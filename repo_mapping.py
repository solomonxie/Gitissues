#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os           # for folder detecting
import sys          
import json
import shutil       # for zipping files
from datetime import date


def main():

    # @@ load local config file
    cfg = os.path.dirname(os.path.realpath(sys.argv[0])) + '/config.json'
    with open(cfg, 'r') as f:
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
    with open(repo_dir+'/issues.json', 'r') as f:
        issues = json.loads(f.read())

    # @@ iterate each issue for further fetching
    for issue in issues:
        title = issue['title']
        info  = issue['body']
        index = issue['number']

        # @@ prepare contents for output markdown file
        fcontents = ['# ' + title + '\n' + info + '\n\n\n']

        # @@ load comments
        with open(repo_dir+'/comments-for-issue-%d.json'%index, 'r') as f:
            comments = json.loads(f.read())

        # @@ consit the content of file with each comment
        for cm in comments:
            fcontents.append( cm['body'] +'\n\n\n' )

        #print 'Generated markdown file for issue-%d[%s].'%(index,title)


        if os.path.exists(repo_dir+'/markdown') is False:
            os.makedirs(repo_dir+'/markdown')

        # @@ output comments into one issue file, named strictly be <ISSUE-INDEX.md>
        with open('%s/markdown/%d.md'%(repo_dir,index), 'w+') as f:
            f.write( '\n\n\n'.join(fcontents).encode('utf-8') )

    print 'Generated %d issues from [%s] to markdown file.'%(len(issues),repo)



if __name__ == "__main__":
    main()
