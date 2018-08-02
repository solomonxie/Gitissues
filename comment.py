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

    def __init__2(self, url):
        """
        Accpet comment's url, as
        independently retrive all self-contained information
        according to the url, without getting information
        from the superior Issue instance.
        """
        self.url = url
        self.api = self.__get_api()
        pass
    
    def __get_api(self):
        """
        Convert normal url to api url.
        URL: https://github.com/{{ username }}/{{ repo }}/issues/{{ issue-index }}#issuecomment-{{ comment-id }}
        API: https://api.github.com/repos/{{ username  }}/{{ repo  }}/issues/comments/{{ comment-id }}
        """
        regex = r'http[s]?://(www\.)?github.com/([^/]+)/([^/]+)/issues/(\d+)'
        result = re.findall(regex, self.url)
        if not result:
            return ''
        res = result[0]
        
        return f'https://api.github.com/repos/{res[1]}/{res[2]}/issues/comments/{res[5]}'

    def __init__(self, cmt, issue):
        self.cfg = issue.cfg
        self.parent = issue.index
        self.id = cmt['id']
        self.body = cmt['body']
        self.title = self.__get_title()
        self.created_at = cmt['created_at']
        self.updated_at = cmt['updated_at']
        self.path_md = f'{issue.dir}/comment-{self.id}.md'
        self.path_html = f'{issue.dir}/comment-{self.id}.html'

        self.content = ''
        self.jekyll_post_path = ''
        self.review_dates = self.__generate_review_dates()


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
    