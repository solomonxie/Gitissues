# -*- coding: utf-8 -*-

import os
import json
import logging

log = logging.getLogger('gitissues.repo_mapping')

# @@ zip the folder for backup
#import shutil       # for zipping files
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

    # @@ check source folder's existance
    if os.path.exists(config.repo_dir) is False: return False

    # @@ load issues
    with open(config.repo_dir+'/issues.json', 'r') as f:
        issues = json.loads(f.read())

    # @@ iterate each issue for further fetching
    for issue in issues:
        title = issue['title']
        info  = issue['body']
        index = issue['number']

        # @@ prepare contents for output markdown file
        fcontents = ['# ' + title + '\n' + info + '\n\n\n']

        # @@ load comments
        with open(config.repo_dir+'/comments-for-issue-%d.json'%index, 'r') as f:
            comments = json.loads(f.read())

        # @@ consit the content of file with each comment
        for cm in comments:
            fcontents.append( cm['body'] +'\n\n\n' )

        #print 'Generated markdown file for issue-%d[%s].'%(index,title)


        if os.path.exists(config.repo_dir+'/markdown') is False:
            os.makedirs(config.repo_dir+'/markdown')

        # @@ output comments into one issue file, named strictly be <ISSUE-INDEX.md>
        with open('%s/markdown/%d.md'%(config.repo_dir,index), 'w+') as f:
            f.write( '\n\n\n'.join(fcontents).encode('utf-8') )

    log.info('Generated %d issues from [%s] to markdown file.'%(len(issues),config.repo))

