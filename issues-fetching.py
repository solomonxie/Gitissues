#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os           # for folder detecting
import json
import shutil       # for zipping files
import requests     # for retrieving web resources
from datetime import date


def main():

    # @@ load local config file
    with open('config.json', 'r') as f:
        config = json.loads(f.read())

    #import pdb; pdb.set_trace() # debugging mode
    # @@ fetch each repo and generate issue files
    for repo in config['fetch']['repos']:
        if fetch_issues(config, repo) is False: 
            print 'Failed to fetch the repo [%s]'%repo



# @@ Fetch one repo's issues @2 archive to a local folder @3 pack into a zip file
def fetch_issues(config={}, repo=''):

    # @@ loading settings from customized configs (json)
    user         = config['fetch']['user']
    root         = config['local']['root_dir']
    access_token = '' #'?access_token='+ config['fetch']['access_token']       # api's authentication token string
    today        = str(date.today())
    #               formated uri. should be formated before use
    issues_url   = 'https://api.github.com/repos/%s/%s/issues%s'
    comments_url = 'https://api.github.com/repos/%s/%s/issues/%d/comments%s'

    #import pdb; pdb.set_trace() # debugging mode

    # @@ retrieving data from internet, @ with response validation
    r      = requests.get(issues_url%(user,repo,access_token),timeout=10)
    if r.status_code is not 200: return False

    # @@ log issues as original json file, for future restoration or further use
    if os.path.exists(root+'/log') is False:
        os.makedirs(root+'/log')
    with open(root+'/log/issues.json', 'w') as f:
        f.write(r.content)

    # @@ iterate each issue for further fetching
    for issue in r.json() :
        title = issue['title']
        info  = issue['body']
        index = issue['number']

        # @@ fetch comments, @ with response validation 
        _r        = requests.get(comments_url%(user,repo,index,access_token),timeout=10)
        if _r.status_code is not 200: continue #or# return False

        # @ log comments as original json file, for future restoration or further use
        with open(root+'/log/comments-for-%d.json'%index, 'w') as f:
            f.write(_r.content)

        print '%d comments for issue[%s] loaded.'%(len(_r.json()), title)

        # @@ check local folder's existance
        if os.path.exists(root) is not True:
            os.makedirs(root)

    print 'all issues fetched.'



if __name__ == "__main__":
    main()
