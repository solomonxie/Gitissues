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
    
    if len(sys.argv) is 1:
        logging.warn('Please indicate the path of config file.')
        return
    
    # @@ load local config file
    with open(sys.argv[1], 'r') as f:
        config = json.loads(f.read())


    fetch_issues(config)


def fetch_issues(config):
    """
    FETCH one repo's issues, @2 archive to a local folder
    IF there's no change from internet, then abord fetching and writing to local files
    """

    log = logging.getLogger('root')

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

    #import pdb; pdb.set_trace()      ## debugging mode

    # @ prepare local git repo for the first time
    if os.path.exists(root) is False:
        log.info('local repo doesn\'t exist, setting up now...')

        os.system('git clone %s %s'%(remote_url, root))
        os.system('git -C %s config credential.helper cache'%root)
        os.system('git -C %s config user.email %s'%(root,email))
        os.system('git -C %s config user.name %s'%(root,remote_user))


    # @@ retrieving data from internet, @ with response validation
    log.info('retriving [%s] now...'%(issues_url+auth))
    r = requests.get(issues_url+auth,timeout=10)

    if r.status_code is not 200:
        log.error('Failed on fetching [%s] due to unexpected response'%issues_url)
        return False

    log.info('Remaining %s requests limit for this hour.'%r.headers['X-RateLimit-Remaining'])

    # @@ REMOVE user directory before download new data. 
    try:
        log.info('clearing previous fetched data on [%s/%s]...'%(root,user))
        #shutil.rmtree(repo_dir) 
        os.system('rm -rf %s/%s'%(root,user))
    except Exception as e:
        log.error(e.message)
        pass


    if os.path.exists(repo_dir+'/src') is False:
        os.makedirs(repo_dir+'/src')

    # @@ log issues as original json file, for future restoration or further use
    with open(repo_dir+'/src/issues.json', 'w') as f:
        f.write(r.content)


    #import pdb; pdb.set_trace() # debugging mode
    
    # @@ iterate each issue for further fetching
    issues = r.json()
    for issue in issues:
        title = issue['title']
        info  = issue['body']
        index = issue['number']
        comments_url = issue['comments_url']
        counts = issue['comments']

        # @@ pause for awhile before fetch to reduce risk of being banned from server
        time.sleep(1)     # sleep 1 sec

        # @@ fetch comments, @ with response validation 
        _r = requests.get(comments_url+auth,timeout=10)
        if _r.status_code is not 200:
            log.error('Failed on fetching [%s] due to enexpected response'%comments_url)
            return False              # if failed one comment, then restart whole process on this issue

        # @@ log comments as original json file, for future restoration or further use
        with open(repo_dir+'/src/issue-%d.json'%index, 'w') as f:
            f.write(_r.content)

        log.info('%d comments for issue-%d[%s] fetched.'%(counts,index, title))

    log.info('all %d issues for %s fetched.'%(len(issues),repo))



if __name__ == "__main__":
    main()
