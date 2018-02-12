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

    # @ loading settings from customized configs (json)
    user = config['fetch']['user']
    root = config['local']['root_dir']
    access_token = '?access_token='+ config['fetch']['access_token']       # api's authentication token string
    # logging fetching date
    today = str(date.today())

    import pdb; pdb.set_trace() # debugging mode
    # @ fetch each repo and generate issue files
    for repo in config['fetch']['repos']:
        #if fetch_issues(config, repo) is False: 
        #    print 'Failed to fetch the repo [%s]'%repo
        repo_dir = '%s/%s/%s'%(root,user,repo)  # specify the backuped repo's path
        if generate_docs(fetch_dir='%s/%s/%s'%(root,user,repo)) is False:
            print 'Failed to fetch the repo [%s]'%repo

    # @@ zip the folder for backup
    shutil.make_archive(
            format   = 'zip',
            base_name= config['zip_dir']+'/'+user+today, # path to load files
            root_dir = root,                             # path to store zip file
            base_dir = user)                             # zip internal folder wrapper

    print 'data archived to %s/%s%s.zip'%(root,user,today)




# @@ Fetch one repo's issues @2 archive to a local folder @3 pack into a zip file
def fetch_issues(config={}, repo=''):

    # formated uri. should be formated before use
    uri_issues   = 'https://api.github.com/repos/%s/%s/issues%s'
    uri_comments = 'https://api.github.com/repos/%s/%s/issues/%d/comments%s'

    #import pdb; pdb.set_trace() # debugging mode

    # @@ retrieving data from internet, @ with response validation
    r      = requests.get(uri_issues%(user,repo,access_token),timeout=10)
    if r.status_code is not 200: return False

    # @@ log issues as original json file, for future restoration or further use
    if os.path.exists(repo_dir+'/log') is not True:
        os.makedirs(repo_dir+'/log')
    with open(repo_dir+'/log/issues.json', 'w') as f:
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
        with open(repo_dir+'/log/comments-of-issue-%d.json'%index, 'w') as f:
            f.write(_r.content)

        print '%d comments for issue[%s] loaded.'%(len(_r.json), title)

        # @@ check local folder's existance
        if os.path.exists(repo_dir) is not True:
            os.makedirs(repo_dir)

    print 'all issues fetched.'



# @ generate issues markdown files from local json files fetched beforehead
def generate_docs(fetch_dir=''):

    # @@ check source folder's existance
    if os.path.exists(fetch_dir) is False: return False

    # @ load issues from local json file 
    with open(fetch_dir+'/log/issues.json', 'r') as f:
        issues = json.loads(f.read())

    # @ iterate each issue for further fetching
    for issue in issues:
        title = issue['title']
        info  = issue['body']
        index = issue['number']

        # @ prepare contents for output markdown file
        fcontents = ['# ' + title + '\n' + info + '\n\n\n']

        # @ load comments
        with open(fetch_dir+'/log/issues.json', 'r') as f:
            comments = json.loads(f.read())

        # @@ consit the content of file with each comment
        for cm in comments:
            fcontents.append( cm['body'] +'\n\n\n' )

        print '%d comments for issue[%s] loaded.'%(len(fcontents), title)


        # @@ output comments into one issue file, named strictly be <ISSUE-INDEX.md>
        with open('%s/%d.md'%(fetch_dir,index), 'w+') as f:
            f.write( '\n\n\n'.join(fcontents).encode('utf-8') )

    print 'all issues file (markdown) generated.'



if __name__ == "__main__":
    main()
