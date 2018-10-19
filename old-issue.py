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
import re
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

        self.dir = self.cfg.get_path_issue_dir(self.index)
        self.local = self.cfg.get_path_issue_local(self.index)
        self.path_raw = self.cfg.get_path_issue_raw(self.index)
        self.path_csv = self.cfg.get_path_issue_csv(self.index)
        self.path_markdown = self.cfg.get_path_issue_markdown(self.index)
        self.path_html = self.cfg.get_path_issue_html(self.index)
        self.path_review = self.cfg.get_path_issue_review_dates_csv(self.index)

        if os.path.exists(self.dir) is False:
            os.makedirs(self.dir)
        if os.path.exists(self.local) is False:
            os.makedirs(self.local)


    def fetch_details(self):
        """
        Retrive an specific issue with detailed information
        """
        # retrive all details of an issue and all its comments
        # @@ retrive comments, @ with response validation 
        r = self.cfg.request_url(self.api)
        if r is None or self.count == '0':
            log.debug('No comments fetched.')
            return False


        self.raw = r.text
        self.json = r.json()
        log.info('Retrived issue-{}[{}][{} comments] successful.'.format(
                    self.index, self.title, self.count))

        # Instantiate each comment
        for c in self.json:
            self.comments.append( Comment(c, self) )
        
        self.__save_data_raw()
        self.__save_comments_list_csv()
        
        log.info('Finished fetching for issue-%s'%self.index)
    

    def __save_data_raw(self):
        with open(self.path_raw, 'w') as f:
            f.write(self.raw)

    def __save_comments_list_csv(self):
        """
        Save an issue's comments-list with csv file
        including comments id and dates
        """
        if len(self.comments) == 0:
            log.warn('No comments of issue-[%s] was found.'%self.index)
            return False

        lines = ['{},{},{}'.format(c.id,c.created_at,c.updated_at) \
                    for c in self.comments]
        content = '\n'.join(lines)

        with open(self.path_csv, 'w+') as f:
            if f.read() != content:
                f.write(content)


    
    def export_to_markdown(self):
        # Export the issues main content
        content = '# %s\n%s'%(self.title, self.desc)
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
        content = '# {} \n {} \n\n\n {}'.format(
            self.title,
            self.desc,
            bodies
        )

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
        # Generate recommaned review dates according to created_at
        csv = []
        for cmt in self.comments:
            csv.append('{},{},{}'.format( \
                ','.join(cmt.review_dates), 
                cmt.title, cmt.path_html))

        with open(self.path_review, 'w') as f:
            f.write('\n'.join(csv))
