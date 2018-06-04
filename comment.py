# -*- coding: utf-8 -*-
# Python3. Preferred in pipenv virtual enviroment.

"""
File: comment.py
Author: Solomon Xie
Email: solomonxiewise@gmail.com
Github: https://github.com/solomonxie
Description: 
"""


import os
import json
import requests
import logging

log = logging.getLogger('gitissues.issue')

class Comment:
    """
    A class for storing & operating comments of an issue
    """

    def __init__(self, config, cm, issue_number):
        self.cfg = config
        self.parent = issue_number
        self.title = str(cm['id'])
        self.id = cm['id']
        self.content = cm['body']
        self.url = cm['url']
        self.link = cm['html_url']
        self.issue_url = cm['issue_url']
        self.mfile = '%s/markdown/comments/%d/comment-%d.md' %(
                self.cfg.repo_dir, self.parent, self.id)

    def create_markdown(self):
        """
        Create an markdown file for this comment
        """
        if os.path.exists(os.path.dirname(self.mfile)) is False:
            os.makedirs(os.path.dirname(self.mfile))

        # @@ prepare contents for outputting markdown file
        output = '# ' + self.title + '\n' + self.content

        # @@ output comments into one issue file, named strictly be <ISSUE-INDEX.md>
        with open(self.mfile, 'w') as f:
            f.write(output)
            log.info('Generated markdown file for comment [%s] at "%s".'%(self.title, self.mfile))

        return output


    def delete(self):
        """
        Delete a comment that no longer exists at remote
        """
        log.warn('Failed to delete. Function "delete" has not yet completed.')

