#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os           # for folder detecting
import json
import shutil       # for zipping files
from datetime import date


def main():

    if len(sys.argv) is 1:
        print 'Please indicate the path of config file.'
        return

    # @@ load local config file
    with open(sys.argv[1], 'r') as f:
        config = json.loads(f.read())

    mapping_repo(config)

    # @@ zip the folder for backup
    #shutil.make_archive(
    #        format   = 'zip',
    #        base_name= config['archive_dir']+'/'+user+str(date.today()), # path to load files
    #        root_dir = root,                             # path to store zip file
    #        base_dir = user)                             # zip internal folder wrapper
    #print 'data archived to %s/%s%s.zip'%(root,user,today)



# @@ map issues from json data to markdown files 
def mapping_repo(config):
    """
    GENERATE json data to markdown files
    """

    # @@ loading settings from customized configs (json)
    user = config['fetch']['user']
    repo = config['fetch']['repo']
    root = config['local']['root_dir']
    repo_dir = '%s/%s/%s'%(root,user,repo)


    # @@ check source folder's existance
    if os.path.exists(repo_dir) is False: return False

    # @@ load issues
    with open(repo_dir+'/src/issues.json', 'r') as f:
        issues = json.loads(f.read())

    # @@ iterate each issue for further fetching
    for issue in issues:
        title = issue['title']
        info  = issue['body']
        index = issue['number']

        # @@ prepare contents for output markdown file
        fcontents = ['# ' + title + '\n' + info + '\n\n\n']

        # @@ load comments
        with open(repo_dir+'/src/issue-%d.json'%index, 'r') as f:
            comments = json.loads(f.read())

        # @@ consit the content of file with each comment
        for cm in comments:
            fcontents.append( cm['body'] +'\n\n\n' )

        print '%d comments for issue-%d[%s] mapped.'%(len(fcontents)-1,index,title)


        # @@ output comments into one issue file, named strictly be <ISSUE-INDEX.md>
        with open('%s/%d.md'%(repo_dir,index), 'w+') as f:
            f.write( '\n\n\n'.join(fcontents).encode('utf-8') )

    print 'all issues for [%s] mapped to markdown file.'%repo



if __name__ == "__main__":
    main()
