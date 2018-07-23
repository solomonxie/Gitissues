# -*- coding: utf-8 -*-
# Python3. Preferred in pipenv virtual enviroment.

"""
File: issues.py
Author: Solomon Xie
Email: solomonxiewise@gmail.com
Github: https://github.com/solomonxie
Description: 
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
    Handling updating/deleting/creating issues-list
    The core part of this project.
    """
    def __init__(self, config):
        self.cfg = config
        self.issues = []
        self.updates = []
        self.deletes = []
        self.modifications = []    # for git commit message ONLY
        self.issues_json = None
        self.issues_text = None
        self.issues_csv = None
        # Retrive issues-list data
        if self.__get_issues_list() is None:
            log.warn('Retriving issues list failed.')
            self = None
            return


    def __get_issues_list(self):
        """
        Retrieving data from internet, @ with response validation
        """
        log.info(f'Now retriving [{self.cfg.issues_url+self.cfg.auth}]...')

        try:
            r = requests.get(self.cfg.issues_url + self.cfg.auth, timeout=5)
        except Exception as e:
            log.error(f'An error occured when requesting from Github:\n{str(e)}')
            log.error('Mission aborted.')
            #log.debug('Response headers are as below:\n%s' % str(r.headers))
            return None

        if r.status_code is not 200:
            log.error(f'Failed on fetching {self.cfg.issues_url} due to unexpected response')
            return None

        # Set up retrived data
        self.issues_json = r.json()
        self.issues_text = r.text

        __limit = r.headers['X-RateLimit-Remaining']
        log.info(f'Remain {__limit} requests limit in this hour.')
        log.info('Retrived issues successfully.')

        # Save retrived data csv file
        self.__save_issues_list_csv()
        log.info('Saved issues_list as [last_issues_list.csv]')
        return r
    
    def __save_issues_list_csv(self):
        """
        """
        content = [] 
        for iss in self.issues_json:
            line = f"{iss['number']}, {iss['id']}, {iss['created_at']}, {iss['updated_at']}, {iss['title']}"
            content.append(line)
        
        # Build directory structure
        if os.path.exists(self.cfg.repo_dir) is False:
            os.makedirs(self.cfg.repo_dir) 
        with open(f'{self.cfg.repo_dir}/last_issues_list.csv', 'w') as f:
            f.write('\n'.join(content))


    def update(self):
        """
        Description:
            Update local stored issues data
        Algorithm:
            Introduced filtering algorithm to avoid updating a non-changed content
        :return integer: number of issues changes
        """
        if self.first_run() is False:
            self.filter_changes()

        self.fetch_issues()

        return len(self.modifications)


    def first_run(self):
        """
        Download everything as local repo's initialization
        """
        # if os.path.exists(self.cfg.last_issues_path) is True:
        #     return False
        
        log.info('First run: Start initializing local repo...')

        # Remove entire local backup-folder if no last issues data
        # if os.path.exists(self.cfg.repo_dir) is True:
        #     os.system('mv %s /tmp' % self.cfg.repo_dir)

        # Treat every issue as an update
        self.updates = [iss['number'] for iss in self.issues_json]
        
        return True


    def filter_changes(self):
        """
        Filter out unchanged issues, only fetch changed issues
        """
        log.info('Filtering updated and deleted items...')
        # @@ match updated issues and deleted items
        with open(self.cfg.issues_path, 'r') as f:
            new = self.issues_json
            old = json.loads(f.read())

        if new is None or old is None:
            log.error('Someting wrong with issues list JSON file. Please check')
            return

        # @@ filter out same issues from deletes that also exist in updates
        self.updates = [n['number'] for n in new if n not in old]
        #self.deletes = [o['number'] for o in old if o not in new and o['number'] not in self.updates]



    def fetch_issues(self):
        """
        Download every updated issue and its comments from the cloud
        """
        log.info('%d updates to be fetched...' % len(self.updates))
        for iss in self.issues_json:
            issue = Issue(self.cfg, iss)
            if issue.index in self.updates: 
                issue.fetch_issue_details()
                issue.create_markdown()
            elif issue.index in self.deletes:
                issue.delete()
            self.modifications.append(issue.title)

    


    def git_pull(self):
        """
        Need to prepare local user content repository always updated with remote before make any change
        Just for avoiding conflict
        """
        # @@ prepare local git repo for the first time
        if os.path.exists(self.cfg.repo_dir) is False:
            log.warn('local repo does not exist, setting up now...')
            with os.popen(f'git clone {self.cfg.remote_url} {self.cfg.root} 2>&1') as p:
                log.info('GIT CLONE:\n'+p.read())

        # @ keep local repo updated with remote before further change to avoid conflict
        log.info('Check git remote status before further updates: ')
        with os.popen(f'git -C {self.cfg.root} pull origin master 2>&1') as p:
            log.info('GIT PULL:\n'+p.read())

        # @Deprecated, use ssh connection instead@        setup default configuration
        #os.system('git -C %s config credential.helper cache'%self.cfg.root)
        #os.system('git -C %s config user.email %s'%(self.cfg.root, self.cfg.email))
        #os.system('git -C %s config user.name %s'%(self.cfg.root, self.cfg.remote_user))

    
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
        with os.popen(f'git -C {self.cfg.root} add . 2>&1') as p:
            log.info('GIT ADDED.')
        with os.popen(f'git -C {self.cft.root} commit -m "{msg}" 2>&1') as p:
            log.info('GIT COMMIT:\n' + p.read())
        with os.popen(f'git -C {self.cfg.root} push origin master 2>&1') as p:
            log.info('GIT PUSH:\n' + p.read())
