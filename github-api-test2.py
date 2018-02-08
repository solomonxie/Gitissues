#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests, json

user = 'solomonxie'
repo = 'gitissues'

r      = requests.get( 'https://api.github.com/repos/%s/%s/issues'%(user,repo) )
issues = json.loads(r.content)

for issue in issues :
    title = issue['title']
    info  = issue['body']
    index = issue['number']

    # 读取本issue的所有comments
    r_ = requests.get( "https://api.github.com/repos/%s/%s/issues/%d/comments"%(user,repo,index) )
    comments  = json.loads(r_.content)
    fcontents = [info + '\n\n\n']
    for cm in comments:
        fcontents.append( cm['body'] +'\n\n\n' )

    print '%d comments for issue[%s] loaded.'%(len(fcontents), title)

    with open('%d-%s.md'%(index, title), 'w') as f:
        f.write( '\n\n\n'.join(fcontents).encode('utf-8') )
