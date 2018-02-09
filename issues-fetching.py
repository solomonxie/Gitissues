#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os           # for folder detecting
import pdb          # for debugging
import json
import shutil       # for zipping files
import requests     # for retrieving web resources
from datetime import date


#pdb.set_trace()     # start debugging mode

# loading settings from customized configs (json)
with open('config.json', 'r') as f:
    config = json.loads( f.read() )
    user       = config['username']
    repo       = config['repos'][0]        # repo's name, could be multiple
    api_token  = config['api_token']       # api's authentication token string
    backup_dir = config['backup_dir']      # backup everything to a place under this folder
    repo_dir   = config['backup_dir'] +'/%s/%s'%(user,repo)  # specify the backuped repo's path
    zip_dir    = config['zip_dir']         # where this zip file will be stored
    uri_issues   = 'https://api.github.com/repos/%s/%s/issues?access_token=%s'                # uri with formats, should be formated before use
    uri_comments = 'https://api.github.com/repos/%s/%s/issues/%d/comments?access_token=%s'    # uri with formats, should be formated before use

# Prepare for fetching logs, means each fetching will be recorded as a log file.
if os.path.exists(repo_dir+'/log') is not True:
    os.mkdir(repo_dir+'/log')

r      = requests.get(uri_issues%(user,repo,api_token))
issues = json.loads(r.content)

# iterate each issue for further fetching
for issue in issues :
    title = issue['title']
    info  = issue['body']
    index = issue['number']

    # fetching a comment list (already include full content for each comment)
    _r        = requests.get(uri_comments%(user,repo,index,api_token))
    comments  = json.loads(_r.content)
    fcontents = [info + '\n\n\n']

    # loop reading each comments
    for cm in comments:
        fcontents.append( cm['body'] +'\n\n\n' )

    print '%d comments for issue[%s] loaded.'%(len(fcontents), title)

    if os.path.exists(repo_dir) is not True:
        os.makedirs(repo_dir)

    # output comments into one issue file, named like <1.A-issue-today.md>
    with open('%s/%d.%s.md'%(repo_dir,index,title), 'w+') as f:
        f.write( '\n\n\n'.join(fcontents).encode('utf-8') )

print 'all issues fetched.'


# zip the folder for backup
shutil.make_archive(
        format   = 'zip',
        base_name= zip_dir+'/'+repo+str(date.today()),        # full output path and name of zip file
        root_dir = backup_dir,                                # folder path to store zip file
        base_dir = user+'/'+repo)                             # internal folder structure in zip file

print 'data archived to %s/%s%s.zip'%(zip_dir,repo, str(date.today()))
