import requests, json

url = 'https://api.github.com/repos/solomonxie/gitissues/issues'

headers = {
    'Cache-Control': 'no-cache'
}

response = requests.request('GET', url, headers=headers)

issues = json.loads( response.text )
# print( type(issues) )

for issue in issues :
#     print( issue['title']  )
#     print( issue['created_at']  )
#     print( issue['labels']  )
#     print( issue['body']  )

    info = '''
---
title: {title}
date: {date}
categories:
- src
- space
layout: post
---
'''
    print( info.format(title=issue['title'], date=issue['created_at'])  )
