# -*- coding: utf-8 -*-
# Python3. Preferred in pipenv virtual enviroment.

"""
Author: Solomon Xie
Email: solomonxiewise@gmail.com
Github: https://github.com/solomonxie
Description: 
Class:
    - Issues
"""


import os
import json
import logging
import requests

# This project's modules
from issue import Issue


log = logging.getLogger('gitissues.issues')


class Issues:
    """
    Handling issues-list
    The core part of this project.
    """
    def __init__(self, config):
        self.cfg = config
        self.api = self.cfg.target_url + self.cfg.auth

        self.issues = []
        self.updates = []
        self.modifications = []    # for git commit message ONLY
        self.issues_json = None
        self.issues_text = None
        self.issues_csv = None

        self.last_issues_list_path  = './.local/last_issues_list.csv' 

        # Retrive issues-list data
        if self.__get_issues_list() is None:
            log.warn('Retriving issues list failed.')
            self = None
            return


    def __get_issues_list(self):
        """
        Retrieving data from internet, @ with response validation
        """
        log.info(f'Now retriving [{self.api}]...')

        try:
            r = requests.get(self.api, timeout=5)

        except Exception as e:
            log.error(f'An error occured when requesting from Github:\n{str(e)}')
            log.error('Mission aborted.')
            return None

        if r.status_code is not 200:
            log.error(f'Failed on fetching {self.api} due to unexpected response')
            __limit = r.headers['X-RateLimit-Remaining']
            log.debug(f'Remain {__limit} requests limit in this hour.')
            return None


        # Set up retrived data
        self.issues_json = r.json()
        self.issues_text = r.text

        log.info('Retrived issues successfully.')

        return r
    

    def update(self):
        """Description: Update local stored issues data
        :return integer: number of issues changes
        """
        # Initializing
        if self.first_run() is False:
            # only do filtering when it's upadting
            self.filter_changes()

        # Request API only for updated issues
        self.fetch_issues()

        # Save data for future comparison
        self.__save_issues_list_csv()

        return len(self.modifications)


    def first_run(self):
        """Download everything as local repo's initialization """

        if os.path.exists(self.cfg.backup_dir) is True:
            return False
        log.info('First run: Start initializing local repo...')

        # Treat every issue as an update
        self.updates = [iss['number'] for iss in self.issues_json]
        
        return True


    def filter_changes(self):
        """Filter out unchanged issues, only fetch changed issues
        Algorithm:
            Introduced filtering algorithm to avoid updating a non-changed content
        """
        if os.path.exists(self.last_issues_list_path) is False:
            log.warn(f'[{self.last_issues_list_path}] not found.')
            return

        log.info('Filtering updated and deleted items...')

        # import pdb;pdb.set_trace()
        with open(self.last_issues_list_path, 'r') as f:
            csv_reader = [ n.split(',') for n in f.read().split('\n') ]
            old = [ [int(row[0]),row[3]] for row in csv_reader ]
            new = [ [n['number'],n["updated_at"]] for n in self.issues_json ]
        
        self.updates = [ n[0] for n in new if n not in old ]


        log.info(f'Filtered out {len(self.updates)} issues to be updated.')



    def fetch_issues(self):
        """
        Download every updated issue and its comments from the cloud
        """
        log.info('%d updates to be fetched...' % len(self.updates))
        for iss in self.issues_json:
            issue = Issue(self.cfg, iss)
            if issue.index in self.updates: 
                issue.fetch_issue_details()
                issue.export_issue_to_markdown()
                issue.save_comments_list_csv()
                issue.export_comments_to_markdown()
                self.modifications.append(issue.title)


    def __save_issues_list_csv(self):
        """
        Save retrived data (only when there's updates)
        Should be run at the end of program,
        we only want to save new data when all has been updated.
        """
        content = [] 
        for iss in self.issues_json:
            line = f"{iss['number']},{iss['id']},{iss['created_at']},{iss['updated_at']},{iss['title']}"
            content.append(line)
        
        # Build directory structure
        if os.path.exists(self.cfg.backup_dir) is False:
            os.makedirs(self.cfg.backup_dir) 
        with open(self.last_issues_list_path, 'w') as f:
            f.write('\n'.join(content))

        log.info('Saved issues_list as [last_issues_list.csv]')



    def git_pull(self):
        """
        Need to prepare local user content repository always updated with 
        remote before make any change
        Just for avoiding conflict
        """
        # @@ prepare local git repo for the first time
        if os.path.exists(self.cfg.backup_dir) is False:
            log.warn('local repo does not exist, setting up now...')
            with os.popen(f'git clone {self.cfg.backup_url} {self.cfg.backup_dir} 2>&1') as p:
                log.info('GIT CLONE:\n'+p.read())

        # @ keep local repo updated with remote before further change to avoid conflict
        log.info('Check git remote status before further updates: ')
        with os.popen(f'git -C {self.cfg.backup_dir} pull origin master 2>&1') as p:
            log.info('GIT PULL:\n'+p.read())

    
    def git_push(self):
        """
        Push changes to remote backup-repo
        """
        if len(self.modifications) < 1:
            log.info('There is no change to push.')
            return

        # Notice: data of modification is from json file which is 'Unicode' 
        # and all others are type of `str`, so needs to unify this one to str
        msg = 'Modified ' + ', '.join(self.modifications)
        # run standard git workflow to push updates
        with os.popen(f'git -C {self.cfg.backup_dir} add . 2>&1') as p:
            log.info('GIT ADDED.')
        with os.popen(f'git -C {self.cfg.backup_dir} commit -m "{msg}" 2>&1') as p:
            log.info('GIT COMMIT:\n' + p.read())
        with os.popen(f'git -C {self.cfg.backup_dir} push origin master 2>&1') as p:
            log.info('GIT PUSH:\n' + p.read())
