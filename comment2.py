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

def main():
    cmt = Comment('https://github.com/solomonxie/solomonxie.github.io/issues/50#issuecomment-411722479')
    cmt.export_to_jekyll_post()


class Comment:
    """
    A class for storing & operating comments of an issue
    """

    def __init__(self, url=None, data=None):
        """
        Accpet comment's url, as
        independently retrive all self-contained information
        according to the url, without getting information
        from the superior Issue instance.
        """
        self.url = url
        self.data = data
        self.api = self.__url_to_api()

        self.issue_index = None
        self.target_user = ''
        self.target_repo = ''

        self.id = None
        self.title = ''
        self.body = ''

        self.__fetch_data()

    
    def __url_to_api(self):
        """
        Convert normal url to api url.
        URL: https://github.com/{{ username }}/{{ repo }}/issues/{{ issue-index }}#issuecomment-{{ comment-id }}
        API: https://api.github.com/repos/{{ username  }}/{{ repo  }}/issues/comments/{{ comment-id }}
        """
        regex = r'http[s]?://(www\.)?github.com/([^/]+)/([^/]+)/issues/(\d+)(#issuecomment-)?(\d+)'
        result = re.findall(regex, self.url)
        if not result:
            return ''
        res = result[0]

        self.target_user = res[1] 
        self.target_repo = res[2]
        self.issue_index = res[3]
        self.id = res[5]

        return f'https://api.github.com/repos/{res[1]}/{res[2]}/issues/comments/{res[5]}'
    

        
    def __fetch_data(self):
        r = self.cfg.request_url(self.api)
        self.raw = r.text
        self.json = r.json()
        log.info(f'Retrived comment-[{self.title}] successful.')

        self.title = self.__get_title()

    def load_from_url(self, url):
        pass
    

    def load_from_json(self, data):
        pass

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
    

    def export_to_jekyll_post(self):
        pass
    

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
    

if __name__ == "__main__":
    main()