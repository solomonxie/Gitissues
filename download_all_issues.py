import os
import requests
from slugify import slugify

from utils.common_utils import read_envfile

os.environ.update(**read_envfile('envfile-local'))
USERNAME = os.environ['GH_USERNAME']
REPO_NAME = os.environ['GH_REPO_NAME']
ISSUES_URL = f'https://api.github.com/repos/{USERNAME}/{REPO_NAME}/issues'
HEADERS = {'Authorization': 'token ' + os.environ['GH_TOKEN']}


def main():
    resp = requests.get(ISSUES_URL, headers=HEADERS)
    for issue in resp.json():
        title = issue['title']
        print(f'Loading issue: [{title}]')
        created_at = issue['created_at']
        tags = ' '.join(['#' + lb['name'].replace(' ', '') for lb in issue['labels']])
        body = issue.get('body') or ''
        content = f'> tags: {tags}\n> created at: {created_at}\n\n{body}'
        issue_dir = f'/tmp/issues_blog/{title}'
        os.makedirs(issue_dir, exist_ok=True)
        open(f'{issue_dir}/README.md', 'w').write(content)
        cm_url = issue['comments_url']
        cm_count = issue['comments']
        cm_limit = 30
        cm_pages = int((cm_count + abs(cm_count % cm_limit - cm_limit)) / cm_limit)
        comment_list = []
        for p in range(1, cm_pages+1):
            cm_resp = requests.get(f'{cm_url}?page={p}&per_page={cm_limit}', headers=HEADERS)
            for cm in cm_resp.json():
                cm_body = cm['body']
                stop = min(max(cm_body.find('\r'), 0), max(cm_body.find('\n'), 0))
                cm_idx = str(len(comment_list) + 1)
                cm_title = cm_idx + '-' + slugify(cm_body[:stop]).strip()
                cm_content = '{}\n\n{}'.format(cm['created_at'], cm_body)
                comment_list.append({
                    'body': cm_body,
                    'title': cm_title,
                    'created_at': cm['created_at'],
                })
                cm_path = f'{issue_dir}/{cm_title[:128]}.md'
                open(cm_path, 'w').write(cm_content)
                print(f'Saved comment to: {cm_path}')
        print('='*80)


if __name__ == '__main__':
    main()
    print('ok.')
