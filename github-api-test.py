#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests, json

url = 'https://api.github.com/repos/solomonxie/gitissues/issues'

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en,zh-CN;q=0.8,zh;q=0.6'
}

response = requests.request('GET', url, headers=headers)

# 处理接收到的文章中文编码 至关重要！！

# cn = '你好'
# ss = cn.decode('utf-8')
# print repr(ss)
# print ss.encode('utf-8')
# with open('test.txt', 'wt') as f:
#     f.write(ss.encode('utf-8'))
# 
# with open('test.txt', 'r') as f:
# 	print( f.read() )
# 

# rsb = response.text.decode('utf-8')  # 不成功 总是反应某个字符无法编译 


# 获取网络内容时候成功 还没试过获取本地内容 
# rsb = ''
# rsb = response.text.encode('utf-8')
# with open('test.md', 'w') as f:
#     f.write(rsb)



# from urllib import quote
# from urllib import unquote
# rsb = quote( str(response.text) )
# # print rsb
# with open('test.md', 'w') as f:
#     f.write( unquote(rsb) )


# exit()

resp = ''
resp = response.text.encode('utf-8')

issues = json.loads( resp )
# print( type(issues) )

for issue in issues :
#     print( issue['title']  )
#     print( issue['created_at']  )
#     print( issue['labels']  )
#     print( issue['body']  )
#     title = ''+ issue['title'].encode('utf-8')
#     date = ''+ issue['created_at'].encode('utf-8')
#     body = '' + issue['body'].encode('utf-8')

    info = '''
title: %s
date: %s
layout: post

%s'''%(issue['title'], issue['created_at'], issue['body'])

    fn = str( issue['number'] )
    with open(fn+'.md', 'w') as f:
        f.write( info.encode('utf-8') )
    
#     with open('.md', 'w') as f:
#         f.write( info )
