import os
import requests
from retry import retry
from logging import Logger
from slugify import slugify

logger = Logger(__name__)

USER = os.environ.get('GITHUB_USER') or 'solomonxie'
REPO = os.environ.get('GITHUB_REPO') or 'solomonxie.github.io'
HEADERS = {'Authorization': 'token ' + os.environ['ACCESS_TOKEN']}

ISSUES_URL = f'https://api.github.com/repos/{USER}/{REPO}/issues'
ROOT = os.environ.get('BAK_ROOT') or './dataset'


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
    path = os.path.join(ROOT, issue['name'], 'README.md')
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))

    with open(path, 'w') as f:
        f.write(issue['body'] + '\n')
    logger.critical('Saved an issue to: ' + path)
    return path


def save_comment(issue, comment):
    comment['name'] = '{}-{}'.format(comment['id'], slugify(comment['body'][:30]))
    path = os.path.join(ROOT, issue['name'], comment['name'] + '.md')
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))

    with open(path, 'w') as f:
        f.write(comment['body'] + '\n')
    logger.critical('\t Saved a comment to: ' + path)
    return path


def main():
    logger.critical('Start running program...')
    issue_list = download_issues()
    for issue in issue_list:
        download_comments(issue)
    logger.critical('Finished whole program.')


if __name__ == '__main__':
    main()
