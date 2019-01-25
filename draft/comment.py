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
import re
import requests
import logging
import datetime

log = logging.getLogger('gitissues.comment')


class Comment:
    """
    A class for storing & operating comments of an issue
    """

    def __init__(self, data, issue):
        self.cfg = issue.cfg
        self.parent = issue.index
        self.id = data['id']
        self.body = data['body']
        self.title = self.__get_title()
        self.content = ''
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.review_dates = self.__generate_review_dates()

        self.path_md = '{}/comment-{}.md'.format(issue.dir, self.id)
        self.path_html = '{}/comment-{}.html'.format(issue.dir, self.id)
        self.jekyll_post_path = ''


    def export(self):
        self.export_to_markdown()
        # self.export_to_html()

    def export_to_markdown(self):
        """
        Export a comment to formatted Markdown document
        """
        content = self.body

        with open(self.path_md, 'w') as f:
            f.write(content)


    def export_to_html(self):
        """
        Export a comment to formatted Markdown document
        """
        _command = 'pandoc --template=Github.html5 "{}" -o "{}"'.format(\
                    self.path_md, self.path_html)
        log.debug(_command)
        with os.popen(_command) as p:
            log.debug(p.read())


    def __generate_review_dates(self):
        format_in = "%Y-%m-%dT%H:%M:%SZ"
        format_out = '%Y-%m-%d'
        init = datetime.datetime.strptime(self.created_at, format_in)
        first = (init + datetime.timedelta(4)).strftime(format_out)
        second = (init + datetime.timedelta(7)).strftime(format_out)
        third = (init + datetime.timedelta(15)).strftime(format_out)
        fourth = (init + datetime.timedelta(31)).strftime(format_out)
        return [first, second, third, fourth]


    def __get_title(self):
        """Load H1 title from Markdown expression"""
        result_h1 = re.findall(r'^#\s+([^\r\n$]+)', self.body)
        result_h2 = re.findall(r'^##\s+(.+)[^\r\n$]+', self.body)
        result_h3 = re.findall(r'^###\s+(.+)[^\r\n$]+', self.body)
        title_h1 = result_h1[0] if result_h1 else ''
        title_h2 = result_h2[0] if result_h2 else ''
        title_h3 = result_h3[0] if result_h3 else ''
        title = title_h1 if title_h1 else title_h2
        title = title if title else title_h3
        return title


    def delete(self):
        """
        Delete a comment that no longer exists at remote
        """
        log.warn('Failed to delete. Function "delete" has not yet completed.')

