#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, requests, json

# Customize repo and local folder for sotrage
user   = 'solomonxie'
repo   = 'gitissues'
folder = '/Volumes/SD/Workspace/autobackup/%s/%s'%(user,repo)

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

    if not os.path.exists(folder):
        os.makedirs(folder)

    # output comments into one issue file, named like <1.A-issue-today.md>
    with open('%s/%d.%s.md'%(folder,index,title), 'w+') as f:
        f.write( '\n\n\n'.join(fcontents).encode('utf-8') )



