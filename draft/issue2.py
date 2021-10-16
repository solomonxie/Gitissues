# -*- coding: utf-8 -*-
# Python3. Preferred in pipenv virtual enviroment.

"""
Author: Solomon Xie
Email: solomonxiewise@gmail.com
Github: https://github.com/solomonxie
"""

import os
import re
import logging

from comment import Comment

log = logging.getLogger('gitissues.issue')


class Issue:
    """
    Description: A class for a single issue, included every property and function for an issue.
    Instance: This class will be instanized when the update() function of Issues class is called.
    Data: All comments of a issue, are stored in 1 single JSON file,
          which means there's no need to further requests for each comment.
    """

    def __init__2(self, url):
        """
        Accpet issue's url, as
        independently retrive all self-contained information
        according to the url, without getting information
        from the superior instance issues-list.
        """
        self.url = url
        self.api = self.__get_api()
        self.api_issue = ''
        self.api_comments = ''
        self.__get_api()
        pass

    def __get_api(self):
        """
        Convert normal url to api url.
        URL: https://github.com/{{ username }}/{{ repo }}/issues/{{ issue-index }}
        API: https://api.github.com/repos/{{ username  }}/{{ repo  }}/issues/{{ issue-index }}
        API-comments: https://api.github.com/repos/{{ username  }}/{{ repo  }}/issues/{{ issue-index }}/comment
        """
        regex = r'http[s]?://(www\.)?github.com/([^/]+)/([^/]+)/issues/(\d+)'
        result = re.findall(regex, self.url)
        if not result:
            return ''
        res = result[0]

        self.api_issue = f'https://api.github.com/repos/{res[1]}/{res[2]}/issues/{res[3]}'
        self.api_comments = f'https://api.github.com/repos/{res[1]}/{res[2]}/issues/{res[3]}/comments'

    def __init__(self, iss, config):
        self.cfg = config
        self.title = iss['title']
        self.index = iss['number']
        self.desc = iss['body']
        self.url = iss['comments_url']
        self.api = self.url + self.cfg.auth
        self.count = iss['comments']

        self.json = None
        self.raw = None
        self.comments = []
        self.updates = []
        self.deletes = []

        self.dir = self.cfg.get_path_issue_dir(self.index)
        self.path_raw = self.cfg.get_path_issue_raw(self.index)
        self.path_csv = self.cfg.get_path_issue_csv(self.index)
        self.path_markdown = self.cfg.get_path_issue_markdown(self.index)
        self.path_html = self.cfg.get_path_issue_html(self.index)
        self.path_review = self.cfg.get_path_issue_review_dates_csv(self.index)

        if os.path.exists(self.dir) is False:
            os.makedirs(self.dir)

    def fetch_details(self):
        """
        Retrive an specific issue with detailed information
        """
        # retrive all details of an issue and all its comments
        # @@ retrive comments, @ with response validation
        r = self.cfg.request_url(self.api)
        self.raw = r.text
        self.json = r.json()
        log.info(f'Retrived issue-{self.index}[{self.title}][{self.count} comments]  successful.')

        # Instantiate each comment
        for c in self.json:
            self.comments.append(Comment(c, self))

        self.__save_data_raw()
        self.__save_comments_list_csv()

        log.info(f'Finished fetching for issue-{self.index}[{self.title}] with {self.count} comments.')

    def __save_data_raw(self):
        with open(self.path_raw, 'w') as f:
            f.write(self.raw)

    def __save_comments_list_csv(self):
        """
        Save an issue's comments-list with csv file
        including comments id and dates
        """
        if len(self.comments) == 0:
            log.warn(f'No comments of issue-[{self.index}] was found.')
            return

        lines = [f'{c.id},{c.created_at},{c.updated_at}' for c in self.comments]
        content = '\n'.join(lines)

        with open(self.path_csv, 'w+') as f:
            if f.read() != content:
                f.write(content)

    def export_to_markdown(self):
        # Export the issues main content
        content = f'# {self.title}\n{self.desc} '
        with open(self.path_markdown, 'w') as f:
            f.write(content)

        # Export all comments
        for cmt in self.comments:
            cmt.export()

    def __filter_changes(self):
        """
        Filter out updated or deleted comments,
        and store their ID in a list.
        """
        self.updates = []
        self.deletes = []

    def export_all_comments_to_markdown(self):
        """
        Export all comments from an issue into ONE markdown file
        """
        # @@ prepare contents for output markdown file
        bodies = '\n\n\n'.join([c.content for c in self.comments])
        content = f'# {self.title} \n {self.desc} \n\n\n {bodies}'

        if os.path.exists(os.path.dirname(self.dir)) is False:
            os.makedirs(os.path.dirname(self.dir))

        # @@ output comments into one issue file, named strictly be <ISSUE-INDEX.md>
        with open(self.path_markdown, 'w') as f:
            f.write(content)

        log.info('Generated markdown file for [%s] at "%s".' % (self.title, self.path_markdown))

    def export_review_dates(self):
        """
        A a list of future dates of each comment for
        study reviewing according to the Forgetting Curve theory
        """
        # Generate recommaned review dates according to created_at
        csv = []
        for cmt in self.comments:
            csv.append('{},{},{}'.format(
                ','.join(cmt.review_dates),
                cmt.title, cmt.path_html))

        with open(self.path_review, 'w') as f:
            f.write('\n'.join(csv))
