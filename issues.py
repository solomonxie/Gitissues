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
        self.json = None
        self.raw = None
        self.issues_csv = None


    def __is_first_run(self):
        # return True
        if os.path.exists(self.cfg.backup_dir) is False or \
            os.path.exists(self.last_issues_list_path) is False:
            self.updates = [iss['number'] for iss in self.json]
            return True
        else:
            return False


    def fetch(self):
        # Update local backup repo before fetching
        self.git_pull()

        # Retrive issues-list data
        log.info('Now retriving [%s]...'%self.api)
        r = self.cfg.request_url(self.api)
        if r is None:
            log.warn('Retriving issues list failed.')
            return False
        log.info('Retrived issues successfully.')

        # Set up retrived data
        self.raw = r.text
        self.json = r.json()

        if self.__is_first_run() is True:
            # First run: treat every issue as update
            self.updates = [iss['number'] for iss in self.json]
        else:
            self.__filter_changes()

        # Request API only for updated issues
        self.__fetch_issues()
        # Save data for future comparison
        self.__save_data_raw()
        self.__save_data_csv()

        log.info('Finished checking for this round.\n')

        # Update remote backup repo when fetching finished
        self.git_push()


    def __filter_changes(self):
        """Filter out unchanged issues, only fetch changed issues
        Algorithm:
            Introduced filtering algorithm to avoid updating a non-changed content
        """
        if os.path.exists(self.last_issues_list_path) is False:
            log.warn('[%s] not found.'%self.last_issues_list_path)
            return

        log.info('Filtering updated and deleted items...')

        # import pdb;pdb.set_trace()
        with open(self.last_issues_list_path, 'r') as f:
            csv_reader = [ n.split(',') for n in f.read().split('\n') ]
            old = [ [int(row[0]),row[3]] for row in csv_reader ]
            new = [ [n['number'],n["updated_at"]] for n in self.json ]
        
        self.updates = [ n[0] for n in new if n not in old ]


        log.info(f'Filtered out {len(self.updates)} issues to be updated.')



    def __fetch_issues(self):
        """
        Download every updated issue and its comments from the cloud
        """
        log.info('%d updates to be fetched...' % len(self.updates))
        for iss in self.json:
            issue = Issue(iss, self.cfg)
            if issue.index in self.updates: 
                issue.fetch_details()
                issue.export_to_markdown()
                issue.export_review_dates()
                self.modifications.append(issue.title)


    def __save_data_csv(self):
        """
        Save retrived data (only when there's updates)
        Should be run at the end of program,
        we only want to save new data when all has been updated.
        """
        content = [] 
        for iss in self.json:
            line = '{},{},{},{},{}'.format(
                iss['number'],
                iss['id'],
                iss['created_at'],
                iss['updated_at'],
                iss['title']
            )
            content.append(line)
        
        # Build directory structure
        if os.path.exists(self.cfg.backup_dir) is False:
            os.makedirs(self.cfg.backup_dir) 
        with open(self.last_issues_list_path, 'w') as f:
            f.write('\n'.join(content))

        log.info(f'Saved list data to {self.last_issues_list_path}')
    

    def __save_data_raw(self):
        with open(self.raw_path, 'w') as f:
            f.write(self.raw)
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
            with os.popen('git clone %s %s 2>&1'%(self.cfg.backup_url, self.cfg.backup_dir)) as p:
                log.info('GIT CLONE:\n'+p.read())

        # @ keep local repo updated with remote before further change to avoid conflict
        log.info('Check git remote status before further updates: ')
        with os.popen('git -C %s pull origin master 2>&1'%self.cfg.backup_dir) as p:
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
        with os.popen('git -C %s add . 2>&1'%self.cfg.backup_dir) as p:
            log.info('GIT ADDED.')
        with os.popen('git -C %s commit -m "%s" 2>&1'%(self.cfg.backup_dir, msg)) as p:
            log.info('GIT COMMIT:\n' + p.read())
        with os.popen('git -C %s push origin master 2>&1'%self.cfg.backup_dir) as p:
            log.info('GIT PUSH:\n' + p.read())
    

if __name__ == '__main__':
    # import pdb;pdb.set_trace()
    issues = Issues('./.local/gitissues-config.json')
    issues.fetch() 