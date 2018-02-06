#!/usr/bin/env python
# -*- coding: utf-8 -*-

def __unicoding__(txt=u'', outsource=False):
    if outsource: 
        if type(txt) == type(u''): 
            # return bytes(txt)
            return txt.encode('utf-8')
        else:
            return txt
    else: # 统一转化为unicode
        if type(txt) == type(u''):
            return txt
        else:
            return unicode(txt)


import requests, json

url = 'https://api.github.com/repos/solomonxie/gitissues/issues'

headers = {
    'Connection': 'keep-alive'
}

response = requests.request('GET', url, headers=headers)

resp = __unicoding__(response.text, True)
# print(type(resp))
issues = json.loads(resp)

for issue in issues :
    info = 'title: %s \ndate: %s \nlayout: post \n%s'%(issue['title'], issue['created_at'], issue['body'])
    number = issue['number'] # Integer
    
    # 读取本issue的所有comments
    url = "https://api.github.com/repos/solomonxie/gitissues/issues/%d/comments"%number
    response = requests.request('GET', url, headers=headers)
    resp = __unicoding__(response.text, True)
    comments = json.loads(resp)
    s_comments = u''
    for comment in comments:
        print comment['url']
        s_comments += '\n\n\n'+ comment['body']

    with open('%d.md'%number, 'w') as f:
        f.write( __unicoding__(info,True) + __unicoding__(s_comments,True) )
    
