import os
import requests
from retry import retry
from slugify import slugify
import shutil

assert os.environ['GH_TOKEN'] is not None

USER = os.environ.get('GH_USER') or 'solomonxie'
REPO = os.environ.get('SRC_REPO') or 'solomonxie.github.io'
BAK_REPO = os.environ.get('BAK_REPO') or 'issues_blog'
HEADERS = {'Authorization': 'token ' + os.environ['GH_TOKEN']}

ISSUES_URL = f'https://api.github.com/repos/{USER}/{REPO}/issues'
ROOT = os.environ.get('BAK_ROOT') or f'/tmp/{BAK_REPO}'
BLOG = os.path.join(ROOT, 'blog')
CACHE = '/tmp/blog'


@retry((Exception, ), tries=3, delay=3, jitter=5)
def init_bak_repo():
    """
    Initialize backup-repo
    """
    print('Initialize backup-repo...')
    if os.path.exists(os.path.join(ROOT, '.git')):
        return
    # raise Exception('Not a git repo for backup: {}'.format(os.path.abspath(ROOT)))
    print(f'git clone --depth 1 git@github.com:{USER}/{BAK_REPO}.git {ROOT}')
    p = os.popen(f'git clone --depth 1 git@github.com:{USER}/{BAK_REPO}.git {ROOT}')
    print(p.read())
    if not os.path.exists(os.path.join(ROOT, '.git')):
        raise Exception('Failed to retrive bak-repo')


@retry((Exception, ), tries=3, delay=3, jitter=5)
def sync_bak_repo():
    print('Fetching backup-repo...')
    p = os.popen(f'git -C {ROOT} reset --hard master')
    print(p.read())
    p = os.popen(f'git -C {ROOT} clean -fd')
    print(p.read())
    p = os.popen(f'git -C {ROOT} pull origin master 2>&1')
    print(p.read())


@retry((Exception, ), tries=3, delay=3, jitter=5)
def publish_bak_repo():
    print('Prepare to publish...')
    # Remove existing blog folder (much easier than diff)
    if os.path.exists(BLOG):
        shutil.rmtree(BLOG)
        # print('Removed existing folder: ' + BLOG)

    # Move newly retrieved files from cache to backup folder
    shutil.move(CACHE, BLOG)
    print('Replaced existing files with newly retrieved files')

    p = os.popen(f'git -C {ROOT} add {ROOT}')
    print(p.read())

    p = os.popen(f'git -C {ROOT} diff master --name-only |cat')
    changed_files = p.read().split()
    print(f'Changed files: {changed_files}')
    titles = [f'[ {i+1} ] ' + fname[:20] for i, fname in enumerate(changed_files)]
    changed_titles = '...; '.join(titles)
    print(f'Updated: {changed_titles}')
    commit_msg = f'Auto-sync Updated {len(changed_files)} files: {changed_titles}'[:50]

    print('Pushing backup-repo...')
    p = os.popen(f'git -C {ROOT} commit -am "{commit_msg}"')
    print(p.read())
    p = os.popen(f'git -C {ROOT} push --force origin master')
    print(p.read())


@retry((Exception, ), tries=3, delay=3, jitter=5)
def download_issues():
    resp = requests.get(ISSUES_URL, headers=HEADERS)
    issue_list = resp.json()
    print(f'Will be retriving for {len(issue_list)} issues')
    for issue in issue_list:
        save_issue_body(issue)

    return issue_list


@retry((Exception, ), tries=3, delay=3, jitter=5)
def download_comments(issue):
    comment_list = []
    base_url = issue['comments_url']
    count, limit = issue['comments'], 30
    pages = int((count + abs(count % limit - limit)) / limit)
    # Pagination
    for page in range(0, pages):
        resp = requests.get(f'{base_url}?page={page + 1}&per_page={limit}', headers=HEADERS)
        comment_list += list(resp.json())
    print(f'\t Retrived {len(comment_list)} comments of issue[{issue["number"]}]')
    for i, comment in enumerate(sorted(comment_list, key=lambda x: x['id'])):
        comment['number'] = i + 1
        save_comment(issue, comment)


def save_issue_body(issue):
    issue['name'] = '{}-{}'.format(issue['number'], slugify(issue['title']))
    print('{} last updated at {}'.format(issue['name'], issue['updated_at']))
    path = os.path.join(CACHE, issue['name'], 'README.md')
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))

    with open(path, 'w') as f:
        f.write(issue['body'] + '\n')
    # print('\t Saved an issue to: ' + path)
    return path


def save_comment(issue, comment):
    comment['name'] = '{}-{}'.format(comment['number'], slugify(comment['body'][:20]))
    path = os.path.join(CACHE, issue['name'], comment['name'] + '.md')
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))

    with open(path, 'w') as f:
        f.write(comment['body'] + '\n')
    # print('\t Saved a comment to: ' + path)
    return path


def main():
    print('Start running program...')
    init_bak_repo()

    issue_list = download_issues()
    for issue in issue_list:
        download_comments(issue)
    print('Finished downloading.')

    sync_bak_repo()
    publish_bak_repo()

    print('Finished whole program.')


if __name__ == '__main__':
    main()
