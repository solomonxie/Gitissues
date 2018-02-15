#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os           # for folder detecting
import sys
import json
import shutil       # for zipping files
import requests     # for retrieving web resources
import logging
import time
from datetime import date


def main():
    
    # @@ load local config file
    with open('config.json', 'r') as f:
        config = json.loads(f.read())


    fetch_issues(config)


def fetch_issues(config):
    """
    FETCH one repo's issues, @2 archive to a local folder
    IF there's no change from internet, then abord fetching and writing to local files
    """


    # @@ loading settings from customized configs (json)
    user         = config['fetch']['user']
    repo         = config['fetch']['repo']
    issues_url   = config['fetch']['issues_url']
    auth         = config['fetch']['auth2_ks']
    remote_url   = config['remote']['https']
    remote_user  = config['remote']['user']
    email        = config['remote']['email']
    root         = config['local']['root_dir']
    repo_dir     = '%s/%s/%s'%(root,user,repo)


    # @ prepare local git repo for the first time
    if os.path.exists(root) is False:
        print('local repo does not exist, setting up now...')

        os.system('git clone %s %s'%(remote_url, root))
        os.system('git -C %s config credential.helper cache'%root)
        os.system('git -C %s config user.email %s'%(root,email))
        os.system('git -C %s config user.name %s'%(root,remote_user))


    # @@ retrieving data from internet, @ with response validation
    print('retriving [%s] now...'%(issues_url+auth))
    r = requests.get(issues_url+auth,timeout=10)

    if r.status_code is not 200:
        print('Failed on fetching [%s] due to unexpected response'%issues_url)
        return False

    print('Remaining %s requests limit for this hour.'%r.headers['X-RateLimit-Remaining'])
    

    # @ match updated issues and deleted items
    print('Matching updated items and deleted items')

    new = r.json()
    with open(repo_dir+'/issues.json', 'r') as f:
        old = json.loads(f.read())

    updates = [n for n in new if n not in old]
    deletes = [o for o in old if o not in new]


    # @ CLEAR items that removed in the remote 
    try:
        for d in deletes:
            os.system('rm %s/issue-%d.json'%(repo_dir,d['number']))
            os.system('rm %s/markdown/%d.md'%(repo_dir,d['number']))

            print('Deleted issue-%d[%s].'%(d['number'],d['title']))
    except Exception as e:

        print(e.message)


    # create local folder for fetching the first time or after deletion
    if os.path.exists(repo_dir) is False:
        os.makedirs(repo_dir)

    #import pdb; pdb.set_trace()      ## debugging mode

    # @@ iterate each issue for further fetching
    for issue in r.json():
        title = issue['title']
        info  = issue['body']
        index = issue['number']
        comments_url = issue['comments_url']
        counts = issue['comments']

        # @@ pause for awhile before fetch to reduce risk of being banned from server
        #time.sleep(1)     # sleep 1 sec

        issue_path = '%s/issue-%d.json'%(repo_dir,index)
        if issue in updates or os.path.exists(issue_path) is not True:

            # @@ fetch comments, @ with response validation 
            _r = requests.get(comments_url+auth,timeout=10)
            if _r.status_code is not 200:
                print('Failed on fetching [%s] due to enexpected response'%comments_url)
                return False              # if failed one comment, then restart whole process on this issue

            # @@ log comments as original json file, for future restoration or further use
            with open(issue_path, 'w') as f:
                f.write(_r.content)

            print('Fetched for issue-%d[%s] with %d comments'%(index,title,counts))

    # @@ save original issues data fetched from github api
    with open(repo_dir+'/issues.json', 'w') as f:
        f.write(r.content)

    print('Updated %d issues for repository [%s].'%(len(updates),repo))



if __name__ == "__main__":
    main()
