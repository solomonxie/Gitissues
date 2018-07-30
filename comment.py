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
        self.path = f'{issue.dir_md}/comment-{self.id}.md'

        self.title = ''
        self.content = ''
        self.jekyll_post_path = ''

        self.review_dates = '&'.join( self.__generate_review_dates() )

    
    def export_comment_to_markdown(self):
        """
        Export a comment to formatted Markdown document
        """
        content = self.body
        
        with open(self.path, 'w') as f:
            f.write(content)


    def delete(self):
        """
        Delete a comment that no longer exists at remote
        """
        log.warn('Failed to delete. Function "delete" has not yet completed.')
    

    def __generate_review_dates(self):
        """
        A a list of future dates for reviewing
        according to the Forgetting Curve theory
        """
        return []