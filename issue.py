# -*- coding: utf-8 -*-
# Python3. Preferred in pipenv virtual enviroment.

"""
Author: Solomon Xie
Email: solomonxiewise@gmail.com
Github: https://github.com/solomonxie
Description: 
Class:
    - Issue
"""

import os # for folder detecting
import json
import requests
import logging

# This project's modules
from comment import Comment
from post import Post

log = logging.getLogger('gitissues.issue')

class Issue:
    """
    Description: A class for a single issue, included every property and function for an issue.
    Instance: This class will be instanized when the update() function of Issues class is called.
    Data: All comments of a issue, are stored in 1 single JSON file, 
          which means there's no need to further requests for each comment.
    """

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

        self.dir = self.cfg.issue_dir.format(self.index)
        self.path_markdown = f'{self.dir}/issue-{self.index}.md'
        self.path_html = f'{self.dir}/issue-{self.index}.html'
        self.path_raw = self.cfg.issue_raw.format(self.index)
        self.path_csv = self.cfg.issue_csv.format(self.index)

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
            self.comments.append( Comment(c, self) )
        
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
        bodies = '\n\n\n'.join( [c.content for c in self.comments] ) 
        content = f'# {self.title} \n {self.desc} \n\n\n {bodies}'

        if os.path.exists(os.path.dirname(self.dir)) is False:
            os.makedirs(os.path.dirname(self.dir))

        # @@ output comments into one issue file, named strictly be <ISSUE-INDEX.md>
        with open(self.path_markdown, 'w') as f:
            f.write(content)

        log.info('Generated markdown file for [%s] at "%s".'%(self.title, self.path_markdown))



    def export_review_dates(self):
        """
        A a list of future dates of each comment for 
        study reviewing according to the Forgetting Curve theory
        """
        # Read dates from local comment-*.csv files

        # Generate recommaned review dates according to created_at

        pass