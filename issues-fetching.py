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
        config = json.loads( f.read() )

    # @@ fetching each repo
    for repo in config['repos']:
        result = fetch_issues(config, repo)
        if result is False: print 'Failed to fetch the repo [%s]'%repo

    import pdb; pdb.set_trace() # debugging mode
    # @ zip the folder for backup
    shutil.make_archive(
            format   = 'zip',
            base_name= config['zip_dir']+'/'+repo+today,        # full output path and name of zip file
            root_dir = config['backup_dir'],                                # folder path to store zip file
            base_dir = user)                             # internal folder structure in zip file

    print 'data archived to %s/%s%s.zip'%(zip_dir,repo,today)




# @@ Fetch one repo's issues @2 archive to a local folder @3 pack into a zip file
def fetch_issues(config={}, repo=''):

    # @@ loading settings from customized configs (json)
    user       = config['username']
    backup_dir = config['backup_dir']      # backup everything to a place under this folder
    repo_dir   = config['backup_dir'] +'/%s/%s'%(user,repo)  # specify the backuped repo's path
    zip_dir    = config['zip_dir']         # where this zip file will be stored
    access_token  = '' # '?access_token='+ config['access_token']       # api's authentication token string
    #        logging fetching date
    today      = str(date.today())
    #        formated uri. should be formated before use
    uri_issues   = 'https://api.github.com/repos/%s/%s/issues%s'
    uri_comments = 'https://api.github.com/repos/%s/%s/issues/%d/comments%s'

    #import pdb; pdb.set_trace() # debugging mode

    # @@ retrieving data from internet, @ with response validation
    r      = requests.get(uri_issues%(user,repo,access_token),timeout=10)
    if r.status_code is not 200: return False

    # @@ log issues as original json file, for future restoration or further use
    if os.path.exists(repo_dir+'/log') is not True:
        os.makedirs(repo_dir+'/log')
    with open(repo_dir+'/log/issues-of-%s.json'%repo, 'w') as f:
        f.write(r.content)

    # @ iterate each issue for further fetching
    for issue in r.json() :
        title = issue['title']
        info  = issue['body']
        index = issue['number']

        # @@ fetch comments, @ with response validation 
        _r        = requests.get(uri_comments%(user,repo,index,access_token),timeout=10)
        if _r.status_code is not 200: continue #or# return False

        # @ log comments as original json file, for future restoration or further use
        with open(repo_dir+'/log/comments-of-%s-issue-%d.json'%(repo,index), 'w') as f:
            f.write(_r.content)

        # @@ prepare contents for output markdown file
        fcontents = ['# ' + title + '\n' + info + '\n\n\n']

        # @@ consit the content of file with each comment
        for cm in _r.json():
            fcontents.append( cm['body'] +'\n\n\n' )

        print '%d comments for issue[%s] loaded.'%(len(fcontents), title)

        # @@ check local folder's existance
        if os.path.exists(repo_dir) is not True:
            os.makedirs(repo_dir)

        # @@ output comments into one issue file, named strictly be <ISSUE-INDEX.md>
        with open('%s/%d.md'%(repo_dir,index), 'w+') as f:
            f.write( '\n\n\n'.join(fcontents).encode('utf-8') )

    print 'all issues fetched.'



#def generate_docs():
#    # @ generate issues markdown files from local json files fetched beforehead
#    print ''


if __name__ == "__main__":
    main()
