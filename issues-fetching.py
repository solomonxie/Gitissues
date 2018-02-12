#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os           # for folder detecting
import json
import shutil       # for zipping files
import requests     # for retrieving web resources
import time
from datetime import date


def main():

    # @@ load local config file
    with open('config.json', 'r') as f:
        config = json.loads(f.read())

    #import pdb; pdb.set_trace() # debugging mode
    # @@ fetch each repo and generate issue files
    for repo in config['fetch']['repos']:
        try:
            fetch_issues(config, repo)
        except NameError:
            print 'Error on fetching the repo[%s], trying to fetch again...'
            fetch_issues(config, repo)



# @@ Fetch one repo's issues @2 archive to a local folder @3 pack into a zip file
def fetch_issues(config={}, repo=''):

    # @@ loading settings from customized configs (json)
    user         = config['fetch']['user']
    root         = config['local']['root_dir']
    repo_dir     = '%s/%s/%s'%(root,user,repo)
    access_token = '' #'?access_token='+ config['fetch']['access_token']       # api's authentication token string
    today        = str(date.today())

    #import pdb; pdb.set_trace() # debugging mode

    # @@ retrieving data from internet, @ with response validation
    url_issues = 'https://api.github.com/repos/%s/%s/issues%s'\
            %(user,repo,access_token)
    r = requests.get(url_issues,timeout=10)
    if r.status_code is not 200:
        raise NameError('Failed on fetching [%s] due to unexpected response'%url_issues)

    # @@ log issues as original json file, for future restoration or further use
    if os.path.exists(repo_dir+'/log') is False:
        os.makedirs(repo_dir+'/log')
    with open(repo_dir+'/log/issues.json', 'w') as f:
        f.write(r.content)

    # @ load issues and record amount for comparision
    issues = r.json()
    n = 0

    # @@ iterate each issue for further fetching
    for issue in issues:
        n    += 1
        title = issue['title']
        info  = issue['body']
        index = issue['number']

        # @ pause for awhile before fetch to reduce risk of being banned from server
        time.sleep(1)     # sleep 60sec

        # @@ fetch comments, @ with response validation 
        url_comments = 'https://api.github.com/repos/%s/%s/issues/%d/comments%s'\
                %(user,repo,index,access_token)
        _r = requests.get(url_comments,timeout=10)
        if _r.status_code is not 200:
            raise NameError('Failed on fetching [%s] due to enexpected response'%url_comments) 

        # @ log comments as original json file, for future restoration or further use
        with open(repo_dir+'/log/issue-%d.json'%index, 'w') as f:
            f.write(_r.content)

        print '%d comments for issue-%d[%s] fetched.'%(len(_r.json())+1,index, title)

    if n == len(issues):
        print 'all %d issues for %s fetched.'%(n,repo)
    else:
        print '[%d] issues not been fetched.'%(len(issues)-n)



if __name__ == "__main__":
    main()
