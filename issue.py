# -*- coding: utf-8 -*-
# Python3. Preferred in pipenv virtual enviroment.

"""
File: issue.py
Author: Solomon Xie
Email: solomonxiewise@gmail.com
Github: https://github.com/solomonxie
Description: 
"""

import os # for folder detecting
import json
import requests
import logging

# This project's modules
from comment import Comment

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
        self.info = iss['body']
        self.url = iss['comments_url']
        self.count = iss['comments']
        self.dir = '%s/issue-%d'% (self.cfg.repo_dir, self.index)
        self.path_json = '%s/issue-%d.json'% (self.dir, self.index)
        self.markdown_path = '%s/markdown/issue-%d.md' % (self.cfg.repo_dir, self.index)
        self.issue_json = None
        self.issue_text = None
        self.updates = []
        self.deletes = []


    def fetch_issue_details(self):
        """
        Retrive an specific issue with detailed information
        """
        # retrive all details of an issue and all its comments
        if self.__get_issue_raw() is None:
            log.warn('Failed to fetch details of the issue [%s].'% self.title)
            self = None
            return
        
        self.__save_comments_list_csv()

        self.__filter_changes()

        log.info('Finished fetching for issue-%d[%s] with %d comments' % (self.index,self.title, self.count))
    

    def __get_issue_raw(self):
        """
        """
        # @@ retrive comments, @ with response validation 
        try:
            r = requests.get(self.url + self.cfg.auth, timeout=5)
        except Exception as e:
            log.error('An error occured when requesting from Github:\n%s' % str(e))
            log.info('Mission aborted.')
            return None

        # if failed, then restart whole process on this issue
        if r.status_code is not 200:
            log.warn('Failed on fetching issue, due to enexpected response: [%s]'% self.url)
            return None
        
        log.info(f'Retrived issue-{self.index}[{self.title}][{self.count}comments]  successful.')
        
        # Set up issue data
        self.issue_json = r.json()
        self.issue_text = r.text
        return r


    def __save_comments_list_csv(self):
        """
        Save an issue's comments-list with csv file
        including comments id and dates
        """
        if len(self.issue_json) == 0:
            log.warn(f'Comments of issue-[{self.index}] was not found.')
            return

        content = ''
        for cmt in self.issue_json:
            content += f'{cmt.id}, {cmt.created_at}, {cmt.updated_at}'
            self.__export_comment_to_markdown(cmt)

        with open(f'{self.repo_dir}/issue-{self.index}-comments.csv') as f:
            f.write(content)
        



    def __filter_changes(self):
        """
        Filter out updated or deleted comments, 
        and store their ID in a list.
        """
        self.updates = []
        self.deletes = []
    
    def __export_comments_to_markdown(self):
        """
        Export a comment to formatted Markdown document
        """
        pass


    def delete(self):
        """
        Delete an issue that no longer exists at remote
        """
        log.warn('Failed to delete. Function "delete" has not yet completed.')








    def create_markdown(self):
        """
        Description:
            Create an markdown file for this issue and its all comments
        functionallity: 
            Load a JSON file including all comments of an issue, 
            then extract title, date, content etc., to create a markdown file
        """
        # @@ load comments from json data retrived awhile ago
        comments = json.loads(self.issue_json)

        # @@ prepare contents for output markdown file
        header = '# ' + self.title + '\n' + self.info + '\n\n\n'
        bodies = [cm['body'] for cm in comments]
        content = header + '\n\n\n'.join(bodies)

        if os.path.exists(os.path.dirname(self.markdown_path)) is False:
            os.makedirs(os.path.dirname(self.markdown_path))

        # @@ output comments into one issue file, named strictly be <ISSUE-INDEX.md>
        with open(self.markdown_path, 'w') as f:
            f.write(content)

        log.info('Generated markdown file for [%s] at "%s".'%(self.title, self.markdown_path))
