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
from config import Config


log = logging.getLogger('gitissues.issues')


class Issues:
    """
    Handling issues-list
    The core part of this project.
    """
    def __init__(self, cfg_path):
        # @@ load local config file
        self.cfg = Config(cfg_path)
        self.api = self.cfg.issues_api
        self.raw_path = self.cfg.issues_raw_path
        self.last_issues_list_path = self.cfg.last_issues_list_path

        self.issues = []
        self.updates = []
        self.modifications = []    # for git commit message ONLY
        self.issues_json = None
        self.issues_raw = None
        self.issues_csv = None



    def fetch(self):
        # Update local backup repo before fetching
        #self.git_pull()

        # Retrive issues-list data
        log.info(f'Now retriving [{self.api}]...')
        r = self.cfg.request_url(self.api)
        if r is None:
            log.warn('Retriving issues list failed.')
            return False
        log.info('Retrived issues successfully.')

        # Set up retrived data
        self.issues_raw = r.text
        self.issues_json = r.json()

        self.__fetch_data()

        log.info('Finished checking for this round.\n')

        # Update remote backup repo when fetching finished
        #self.git_push()


    def __fetch_data(self):
        if os.path.exists(self.cfg.backup_dir) is False or \
            os.path.exists(self.last_issues_list_path) is False:
            self.updates = [iss['number'] for iss in self.issues_json]
        else:
            self.filter_changes()
        
        # Request API only for updated issues
        self.fetch_issues()
        # Save data for future comparison
        self.__save_data_raw()
        self.__save_data_csv()


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
            issue = Issue(iss, self.cfg)
            if issue.index in self.updates: 
                issue.fetch_details()
                issue.export_to_markdown()
                self.modifications.append(issue.title)


    def __save_data_csv(self):
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

        log.info(f'Saved list data to {self.last_issues_list_path}')
    

    def __save_data_raw(self):
        with open(self.raw_path, 'w') as f:
            f.write(self.issues_raw)
        log.info(f'Saved raw data to {self.raw_path}')



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
    

if __name__ == '__main__':
    issues = Issues('./.local/gitissues-config.json')
    issues.fetch() 