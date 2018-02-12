#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os           # for folder detecting
import json
import shutil       # for zipping files
from datetime import date


def main():

    # @@ load local config file
    with open('config.json', 'r') as f:
        config = json.loads(f.read())

    # @ loading settings from customized configs (json)
    user = config['fetch']['user']
    root = config['local']['root_dir']
    # indicate mapping date
    today = str(date.today())

    import pdb; pdb.set_trace() # debugging mode
    # @ fetch each repo and generate issue files
    for repo in config['fetch']['repos']:
        if mapping_repo('%s/%s/%s'%(root,user,repo)) is False:
            print 'Failed to fetch the repo [%s]'%repo

    # @@ zip the folder for backup
    shutil.make_archive(
            format   = 'zip',
            base_name= config['zip_dir']+'/'+user+today, # path to load files
            root_dir = root,                             # path to store zip file
            base_dir = user)                             # zip internal folder wrapper

    print 'data archived to %s/%s%s.zip'%(root,user,today)



# @ map issues from json data to markdown files 
def mapping_repo(fetch_dir=''):

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
