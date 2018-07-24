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

class Post:
    """
    """

    def __init__(self, content):
        self.original_url = ''
        self.title = ''
        self.body = ''
        self.tags = []
        self.categories = []
        self.updated_at = ''
        self.created_at = ''
        self.thumbnail = ''
        self.jekyll_front_matter = self.__get_jekyll_front_matter()
    

    def __get_jekyll_front_matter(sefl):
        # return f'---\nlayout: post\ntitle: {}\n date: {}\nimage: {} description: {}\n tags: {}\ncategories: {}\n---'
        return f'''---
        layout: post
        title: {self.title}
        date: {self.updated_at}
        description: 
        tags: \n\t- {"\n\t- ".join(self.tags)}
        categories: \n\t- {"\n\t- ".join(self.categories)}
        ---'''
        


    def export_to_markdown(self):
        """
        """
        pass
    

    def export_to_jekyll_post(self):
        """
        """
        pass