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

log = logging.getLogger('gitissues.comment')

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


    def delete(self):
        """
        Delete a comment that no longer exists at remote
        """
        log.warn('Failed to delete. Function "delete" has not yet completed.')

