#!/usr/bin/env python3
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

def main():
    url = 'https://github.com/solomonxie/solomonxie.github.io/issues/50#issuecomment-418060445'
    cmt = Comment(url)


class Comment:
    """
    """

    def __init__(self, url, json=''):
        pass

    def load_from_local(self, path):
        pass

    def load_from_url(self, url):
        pass

    def load_from_json(self, path):
        pass

    def get_title(self):
        pass

    def get_links(self):
        pass

    def get_images(self):
        pass

    def download_images(self):
        pass

    def save_content(self):
        pass

    def git_push_changes(self):
        pass

    def rewrite_links(self):
        pass

    def set_front_matter(self):
        pass

    def convert_to_html(self):
        pass

    def convert_to_jekyll_post(self):
        pass

    def convert_to_gitbook(self):
        pass

    def sent_email(self):
        pass

    def get_notify_dates(self):
        pass


if __name__ == '__main__':
    main()
