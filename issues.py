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


    def update(self):
        """
        Description:
            Update local stored issues data
        Algorithm:
            Introduced filtering algorithm to avoid updating a non-changed content
        :return integer: number of issues changes
        """
        if self.first_run() is True:
            return len(self.modifications)
        
        self.filter_changes()

        self.__save_last_rettrived()

        self.fetch_issues()

        return len(self.modifications)


    def first_run(self):
        """
        Download everything as local repo's initialization
        """
        if os.path.exists(self.cfg.issues_path) is True:
            return False
        
        log.info('First run: Start initializing local repo...')

        # Remove entire local backup-folder if no last issues data
        os.system('mv %s /tmp' % self.cfg.repo_dir)      
        # Build directory structure
        os.makedirs(self.cfg.repo_dir)
        
        # create local issues data file
        with open(self.cfg.issues_path, 'w') as f:
            f.write(r.text)

        for iss in self.issues_json:
            issue = Issue(self.cfg, iss)
            issue.get_comments()
            self.modifications.append(issue.title)

        return len(issues)


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
        self.deletes = [o['number'] for o in old if o not in new and o['number'] not in self.updates]



    def fetch_issues(self):
        """
        1. Download every issue and its comments from the cloud
        2. Delete issues that was removed on the cloud
        # iterate each issue to update or delete
        # only retrive issues that needed to be updated,
        # avoid to request from Github too many times
        """
        log.info('%d updates to be fetched...' % len(self.updates))
        log.info('%d deletes to be executed...' % len(self.deletes))
        for iss in self.issues_json:
            issue = Issue(self.cfg, iss)
            if issue.index in self.deletes:
                issue.delete()
                self.modifications.append(issue.title)
            elif issue.index in self.updates: 
                issue.get_comments()
                issue.create_markdown()
                self.modifications.append(issue.title)


    def __save_last_rettrived(self):
        """
        """
        # Update local issues raw json file 
        # This step SHOULD BE placed after filtering all updates
        # means no data will be written into file if there's no updates
        with open(self.cfg.issues_path) as f:
            f.write(self.issues_json)
        
        # save csv data file
        with open(self.cfg.repo_dir+'/all-comments.csv') as f:
            f.write(self.issues_csv)

    
    def __get_issues_list(self):
        """
        Retrieving data from internet, @ with response validation
        """
        log.info('Now retriving [%s]...' \
                % (self.cfg.issues_url + self.cfg.auth))

        try:
            r = requests.get(self.cfg.issues_url + self.cfg.auth, timeout=5)
        except Exception as e:
            log.error('An error occured when requesting from Github:\n%s' % str(e))
            log.error('Mission aborted.')
            #log.debug('Response headers are as below:\n%s' % str(r.headers))
            return None

        if r.status_code is not 200:
            log.error('Failed on fetching [%s] due to unexpected response' \
                    % self.cfg.issues_url)
            return None

        log.info('Retrived issues successfully. Remaining %s requests limit for this hour.' \
                % r.headers['X-RateLimit-Remaining'])

        # Set up retrived data
        self.issues_json = r.json()
        self.issues_text = r.text
        self.__set_issues_csv()
        return r
    

    def __set_issues_csv(self):
        """
        """
        pass



    def git_pull(self):
        """
        Need to prepare local user content repository always updated with remote before make any change
        Just for avoiding conflict
        """
        # @@ prepare local git repo for the first time
        if os.path.exists(self.cfg.repo_dir) is False:
            log.warn('local repo does not exist, setting up now...')
            with os.popen('git clone %s %s 2>&1' % (self.cfg.remote_url, self.cfg.root)) as p:
                log.info('GIT CLONE:\n'+p.read())

        # @ keep local repo updated with remote before further change to avoid conflict
        log.info('Check git remote status before further updates: ')
        with os.popen('git -C %s pull origin master 2>&1' % (self.cfg.root)) as p:
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
        with os.popen('git -C %s add . 2>&1' % cfg.root) as p:
            log.info('GIT ADDED.')
        with os.popen('git -C %s commit -m "%s" 2>&1' % (cfg.root, msg)) as p:
            log.info('GIT COMMIT:\n' + p.read())
        with os.popen('git -C %s push origin master 2>&1' % cfg.root) as p:
            log.info('GIT PUSH:\n' + p.read())
