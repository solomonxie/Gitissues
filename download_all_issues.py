import os
import requests

from utils.common_utils import read_envfile

os.environ.update(**read_envfile('envfile-local'))
USERNAME = os.environ['GH_USERNAME']
REPO_NAME = os.environ['GH_REPO_NAME']
ISSUES_URL = f'https://api.github.com/repos/{USERNAME}/{REPO_NAME}/issues'
HEADERS = {'Authorization': 'token ' + os.environ['GH_TOKEN']}


def main():
    resp = requests.get(ISSUES_URL, headers=HEADERS)
    issue_list = resp.json()
    for issue in issue_list:
        issue_title = issue['title']
        created_at = issue['created_at']
        lables = sorted([lb['name'] for lb in issue['labels']])
        cm_url = issue['comments_url']
        cm_count = issue['comments']
        cm_limit = 30
        cm_pages = int((cm_count + abs(cm_count % cm_limit - cm_limit)) / cm_limit)
        comment_list = []
        for p in range(0, cm_pages):
            cm_resp = requests.get(f'{cm_url}?page={p+1}&per_page={cm_limit}', headers=HEADERS)
            comment_list += [{'body': cm['body'], 'created_at': cm['created_at']} for cm in cm_resp.json()]


if __name__ == '__main__':
    main()
