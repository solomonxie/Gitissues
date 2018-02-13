#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os           # for folder detecting
import json
import shutil       # for zipping files
import requests     # for retrieving web resources
import time
from datetime import date


def main():
    
    fetch_issues()


def fetch_issues():
    """
    FETCH one repo's issues, @2 archive to a local folder
    IF there's no change from internet, then abord fetching and writing to local files
    """

    # @@ load local config file
    with open('config.json', 'r') as f:
        config = json.loads(f.read())

    # @@ loading settings from customized configs (json)
    user         = config['fetch']['user']
    repo         = config['fetch']['repo']
    issues_url   = config['fetch']['issues_url']
    root         = config['local']['root_dir']
    repo_dir     = '%s/%s/%s'%(root,user,repo)
    today        = str(date.today())


    # @@ retrieving data from internet, @ with response validation
    r = requests.get(issues_url,timeout=10)
    if r.status_code is not 200:
        print 'Failed on fetching [%s] due to unexpected response'%issues_url
        return False

    # @@ clear directory before download new data. 
    shutil.rmtree(repo_dir) 


    if os.path.exists(repo_dir+'/log') is False:
        os.makedirs(repo_dir+'/log')

    # @@ log issues as original json file, for future restoration or further use
    with open(repo_dir+'/log/issues.json', 'w') as f:
        f.write(r.content)


    #import pdb; pdb.set_trace() # debugging mode
    
    # @@ iterate each issue for further fetching
    issues = r.json()
    for issue in r.json():
        title = issue['title']
        info  = issue['body']
        index = issue['number']
        comments_url = issue['comments_url']
        counts = issue['comments']

        # @@ pause for awhile before fetch to reduce risk of being banned from server
        time.sleep(1)     # sleep 60sec

        # @@ fetch comments, @ with response validation 
        _r = requests.get(comments_url,timeout=10)
        if _r.status_code is not 200:
            print 'Failed on fetching [%s] due to enexpected response'%comments_url
            return False              # if failed one comment, then restart whole process on this issue

        # @@ log comments as original json file, for future restoration or further use
        with open(repo_dir+'/log/issue-%d.json'%index, 'w') as f:
            f.write(_r.content)

        print '%d comments for issue-%d[%s] fetched.'%(len(_r.json())+1,index, title)

    print 'all %d issues for %s fetched.'%(counts,repo)



if __name__ == "__main__":
    main()
