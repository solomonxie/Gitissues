#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, requests, json, shutil
from datetime import date

# loading configs from local json file 
with open('config.json', 'r') as f:
    config = json.loads( f.read() )



# Customize repo and local folder for sotrage
user       = config['username']
repo       = config['repos'][1]
backupto   = config['backupto']
zipto      = config['zipto']
repo_dir   = config['backupto'] +'/%s/%s'%(user,repo)

r      = requests.get( 'https://api.github.com/repos/%s/%s/issues'%(user,repo) )
issues = json.loads(r.content)

# iterate each issue for further fetching
for issue in issues :
    title = issue['title']
    info  = issue['body']
    index = issue['number']

    # fetching a comment list (already include full content for each comment)
    r_        = requests.get( "https://api.github.com/repos/%s/%s/issues/%d/comments"%(user,repo,index) )
    comments  = json.loads(r_.content)
    fcontents = [info + '\n\n\n']
    # loop reading each comments
    for cm in comments:
        fcontents.append( cm['body'] +'\n\n\n' )

    print '%d comments for issue[%s] loaded.'%(len(fcontents), title)

    if not os.path.exists(repo_dir):
        os.makedirs(repo_dir)

    # output comments into one issue file, named like <1.A-issue-today.md>
    with open('%s/%d.%s.md'%(repo_dir,index,title), 'w+') as f:
        f.write( '\n\n\n'.join(fcontents).encode('utf-8') )

print 'all issues fetched.'

# zip the folder for backup
shutil.make_archive(
        format   = 'zip',
        base_name= zipto+'/'+repo, # full output path and name of zip file
        root_dir = backupto, # folder path to store zip file
        base_dir = repo) # internal folder structure in zip file

print 'data archived to %s/%s.zip'%(zipto,repo)
