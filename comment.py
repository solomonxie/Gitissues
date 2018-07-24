# -*- coding: utf-8 -*-
# Python3. Preferred in pipenv virtual enviroment.

"""
Author: Solomon Xie
Email: solomonxiewise@gmail.com
Github: https://github.com/solomonxie
Description: 
Class:
    - Comment
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

    def __init__(self, cmt, issue):
        self.cfg = issue.cfg
        self.parent = issue.index
        self.id = cmt['id']
        self.body = cmt['body']
        self.created_at = cmt['created_at']
        self.updated_at = cmt['updated_at']
        self.markdown_dir = f'{self.cfg.backup_dir}/markdown/issue-{self.parent}'

        self.title = ''
        self.content = ''
        self.jekyll_post_path = ''


    
    def export_comment_to_markdown(self):
        """
        Export a comment to formatted Markdown document
        """
        if os.path.exists(self.markdown_dir) is False:
            os.makedirs(self.markdown_dir)
        
        content = self.body
        
        __path = f'{self.markdown_dir}/comment-{self.id}.md'
        with open(__path, 'w') as f:
            f.write(content)


    def delete(self):
        """
        Delete a comment that no longer exists at remote
        """
        log.warn('Failed to delete. Function "delete" has not yet completed.')

