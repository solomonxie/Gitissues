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

    def __init__(self, config, iss):
        self.cfg = config
        self.title = iss['title']
        self.index = iss['number']
        self.desc = iss['body']
        self.url = iss['comments_url']
        self.api = self.url + self.cfg.auth
        self.count = iss['comments']

        self.comments = []
        self.updates = []
        self.deletes = []

        self.dir_md = f'{self.cfg.backup_dir}/markdown/[{self.cfg.target_user}][{self.cfg.target_repo}]-issue-{self.index}'
        self.path = f'{self.dir_md}/issue-{self.index}.md'
        self.path_comments_list = f'./.local/issue-{self.index}.csv'

        if os.path.exists(self.dir_md) is False:
            os.makedirs(self.dir_md)


    def fetch_issue_details(self):
        """
        Retrive an specific issue with detailed information
        """
        # retrive all details of an issue and all its comments
        __response = self.__get_issue_raw()

        if __response is None:
            log.warn(f'\nFailed to fetch details of the issue [{self.title}].')
            self = None
            return
        
        log.info(f'Finished fetching for issue-{self.index}[{self.title}] with {self.count} comments.')
    

    def __get_issue_raw(self):
        """
        Request API for raw data of an issue
        """
        # @@ retrive comments, @ with response validation 
        try:
            r = requests.get(self.api, timeout=5)

        except Exception as e:
            log.error('An error occured when requesting from Github:\n%s' % str(e))
            log.info('Mission aborted.')
            return None

        # if failed, then restart whole process on this issue
        if r.status_code is not 200:
            log.warn('Failed on fetching issue, due to enexpected response: [%s]'% self.url)
            return None
        
        log.info(f'Retrived issue-{self.index}[{self.title}][{self.count} comments]  successful.')
        
        # Instantiate each comment
        for c in r.json():
            self.comments.append( Comment(c, self) )
        return r


    def save_comments_list_csv(self):
        """
        Save an issue's comments-list with csv file
        including comments id and dates
        """
        if len(self.comments) == 0:
            log.warn(f'No comments of issue-[{self.index}] was found.')
            return

        lines = [f'{c.id},{c.created_at},{c.updated_at}' for c in self.comments]
        content = '\n'.join(lines)

        with open(self.path_comments_list, 'w+') as f:
            if f.read() != content:
                f.write(content)


    
    def export_issue_to_markdown(self):
        """
        """
        content = f'# {self.title}\n{self.desc} '
        with open(self.path, 'w') as f:
            f.write(content)




    def export_comments_to_markdown(self):
        for cmt in self.comments:
            cmt.export_comment_to_markdown()



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

        if os.path.exists(os.path.dirname(self.path)) is False:
            os.makedirs(os.path.dirname(self.path))

        # @@ output comments into one issue file, named strictly be <ISSUE-INDEX.md>
        with open(self.path, 'w') as f:
            f.write(content)

        log.info('Generated markdown file for [%s] at "%s".'%(self.title, self.path))
