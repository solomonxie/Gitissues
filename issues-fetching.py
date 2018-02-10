#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os           # for folder detecting
import json
import shutil       # for zipping files
import requests     # for retrieving web resources
from datetime import date


def main():

    with open('config.json', 'r') as f:
        config = json.loads( f.read() )

    # fetching each repo
    for repo in config['repos']:
        fetch_issues(config, repo)


# @1 Fetch one repo's issues @2 archive to a local folder @3 pack into a zip file
def fetch_issues(config={}, repo=''):

    # loading settings from customized configs (json)
    user       = config['username']
    api_token  = config['api_token']       # api's authentication token string
    backup_dir = config['backup_dir']      # backup everything to a place under this folder
    repo_dir   = config['backup_dir'] +'/%s/%s'%(user,repo)  # specify the backuped repo's path
    zip_dir    = config['zip_dir']         # where this zip file will be stored
    # logging fetching date
    today      = str(date.today())
    # formated uri. should be formated before use
    uri_issues   = 'https://api.github.com/repos/%s/%s/issues?access_token=%s'
    uri_comments = 'https://api.github.com/repos/%s/%s/issues/%d/comments?access_token=%s'

    #import pdb; pdb.set_trace() # debugging mode

    # retrieving data from internet
    r      = requests.get(uri_issues%(user,repo,api_token),timeout=10)
    issues = json.loads(r.content)

    # logging issue list for future comparing
    #if os.path.exists(repo_dir+'/log') is not True:
    #    os.makedirs(repo_dir+'/log')
    #with open(repo_dir+'/log/issues-last-fetching.json', 'w') as f:
    #    f.write(r.content)

    # iterate each issue for further fetching
    for issue in issues :
        title = issue['title']
        info  = issue['body']
        index = issue['number']

        # fetching a comment list (it already includes full content for each comment)
        _r        = requests.get(uri_comments%(user,repo,index,api_token),timeout=10)
        comments  = json.loads(_r.content)
        fcontents = ['# ' + title + '\n' + info + '\n\n\n']

        # loop reading each comments
        for cm in comments:
            fcontents.append( cm['body'] +'\n\n\n' )

        print '%d comments for issue[%s] loaded.'%(len(fcontents), title)

        if os.path.exists(repo_dir) is not True:
            os.makedirs(repo_dir)

        # output comments into one issue file, named strictly be <ISSUE-INDEX.md>
        with open('%s/%d.md'%(repo_dir,index), 'w+') as f:
            f.write( '\n\n\n'.join(fcontents).encode('utf-8') )

    print 'all issues fetched.'

    # zip the folder for backup
    shutil.make_archive(
            format   = 'zip',
            base_name= zip_dir+'/'+repo+today,        # full output path and name of zip file
            root_dir = backup_dir,                                # folder path to store zip file
            base_dir = user+'/'+repo)                             # internal folder structure in zip file

    print 'data archived to %s/%s%s.zip'%(zip_dir,repo,today)



if __name__ == "__main__":
    main()
