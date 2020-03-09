import os
import requests
from retry import retry
from logging import Logger
from slugify import slugify
import shutil

logger = Logger(__name__)

USER = os.environ.get('GITHUB_USER') or 'solomonxie'
REPO = os.environ.get('GITHUB_REPO') or 'solomonxie.github.io'
BAK_REPO = os.environ.get('GITHUB_REPO') or 'git@github.com:solomonxie/issues_blog.git'
HEADERS = {'Authorization': 'token ' + os.environ['TOKEN']}

ISSUES_URL = f'https://api.github.com/repos/{USER}/{REPO}/issues'
ROOT = os.environ.get('BAK_ROOT') or '/tmp'
BLOG = os.path.join(ROOT, 'blog')
CACHE = '/tmp/blog'


@retry((Exception, ), tries=3, delay=3, jitter=5)
def init_bak_repo():
    """
    Initialize backup-repo
    """
    if os.path.exists(os.path.join(ROOT, '.git')):
        return
    # raise Exception('Not a git repo for backup: {}'.format(os.path.abspath(ROOT)))
    p = os.popen('git clone --depth 1 {BAK_REPO} {ROOT} 2>&1')
    logger.critical(p.read())


@retry((Exception, ), tries=3, delay=3, jitter=5)
def sync_bak_repo():
    p = os.popen('git -C {ROOT} reset --hard master')
    logger.critical(p.read())
    p = os.popen('git -C {ROOT} clean -fd')
    logger.critical(p.read())
    p = os.popen('git -C {ROOT} pull origin master 2>&1')
    logger.critical(p.read())


@retry((Exception, ), tries=3, delay=3, jitter=5)
def publish_bak_repo():
    p = os.popen('git -C {ROOT} add . 2>&1')
    logger.critical(p.read())
    p = os.popen('git -C {ROOT} commit -m "Auto-sync with repo {USER}/{REPO}" 2>&1')
    logger.critical(p.read())
    p = os.popen('git -C {ROOT} push --force origin master 2>&1')
    logger.critical(p.read())


@retry((Exception, ), tries=3, delay=3, jitter=5)
def download_issues():
    resp = requests.get(ISSUES_URL, headers=HEADERS)
    issue_list = resp.json()
    logger.critical(f'Retrived {len(issue_list)} issues')
    for issue in issue_list:
        save_issue_body(issue)

    return issue_list


@retry((Exception, ), tries=3, delay=3, jitter=5)
def download_comments(issue):
    resp = requests.get(issue['comments_url'], headers=HEADERS)
    comment_list = resp.json()
    logger.critical(f'Retrived {len(comment_list)} comments')
    for comment in comment_list:
        save_comment(issue, comment)


def save_issue_body(issue):
    issue['name'] = '{}-{}'.format(issue['number'], slugify(issue['title']))
    path = os.path.join(CACHE, issue['name'], 'README.md')
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))

    with open(path, 'w') as f:
        f.write(issue['body'] + '\n')
    logger.critical('Saved an issue to: ' + path)
    return path


def save_comment(issue, comment):
    comment['name'] = '{}-{}'.format(comment['id'], slugify(comment['body'][:30]))
    path = os.path.join(CACHE, issue['name'], comment['name'] + '.md')
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))

    with open(path, 'w') as f:
        f.write(comment['body'] + '\n')
    logger.info('\t Saved a comment to: ' + path)
    return path


def main():
    logger.critical('Start running program...')
    init_bak_repo()

    issue_list = download_issues()
    for issue in issue_list:
        download_comments(issue)
    logger.critical('Finished downloading.')

    # Remove existing blog folder (much easier than diff)
    if os.path.exists(BLOG):
        shutil.rmtree(BLOG)
        logger.critical('Removed existing folder: ', + BLOG)

    # Move newly retrieved files from cache to backup folder
    shutil.move(CACHE, BLOG)
    logger.critical('Replaced existing files with newly retrieved files')

    # Update Git backup-repo
    sync_bak_repo()
    publish_bak_repo()

    logger.critical('Finished whole program.')


if __name__ == '__main__':
    main()
