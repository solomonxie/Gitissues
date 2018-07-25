# -*- coding: utf-8 -*-
# Python3. Preferred in pipenv virtual enviroment.

"""
Author: Solomon Xie
Email: solomonxiewise@gmail.com
Github: https://github.com/solomonxie
Description: 
    Form out a post from Markdown content 
    for Jekyll or other blogging service.
Class:
    - Post
"""

import os
import re
import yaml
import logging

log = logging.getLogger('gitissues.post')



class Post:
    """
    """

    def __init__(self, content=None, title=None):
        if content is None: 
            log.error('Post Content should not be empty.')
            return None
        self.original_url = ''
        self.original_content = content
        self.title = title if title != None else self.__get_title()
        self.body = ''
        self.tags = []
        self.categories = []
        self.updated_at = ''
        self.created_at = ''
        self.thumbnail = ''
        self.jekyll_front_matter = self.__get_jekyll_front_matter()
    

    def __get_jekyll_front_matter(self):
        """Match something like this
        <!--JEKYLL-FRONT-MATTER(will-jekyll-theme)
        ---
        layout: post
        title: 
        image: 
        description: 
        categories:
            - Calculus
        ---
        -->
        """
        # return f'---\nlayout: post\ntitle: {}\n date: {}\nimage: {} description: {}\n tags: {}\ncategories: {}\n---'
        regex = r'^\s*<!--.*\n^---$([\w\W]*)^---$\n-->\s*$'
        _front_matter = ''
        
        return _front_matter
    
    def __get_title(self):
        regex = r'^\#\s+.+$' 
        _title = ''
        return _title
        


    def export_to_markdown(self):
        """
        """
        pass
    

    def export_to_jekyll_post(self):
        """
        """
        pass