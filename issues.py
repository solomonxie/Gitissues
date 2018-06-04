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

        # Sync with cloud before any changes, git pull at very beginning
        self.git_update()


    def update(self):
        """
        Description:
            Update local stored issues data
        Algorithm:
            Introduced filtering algorithm to avoid updating a non-changed content
        """
        if os.path.exists(self.cfg.issues_path) is False:
            os.system('mv %s /tmp' % self.cfg.repo_dir)      # clear workplace by removing
            self.first_run()
            return

        r = self.retrive_data()
        if r is None:
            return 0

        log.info('Filtering updated and deleted items...')
        # @@ match updated issues and deleted items
        with open(self.cfg.issues_path, 'r') as f:
            new = r.json()
            old = json.loads(f.read())

        if new is None or old is None:
            log.error('Someting wrong with issues list JSON file. Please check')
            return

        # @@ filter out same issues from deletes that also exist in updates
        self.updates = [n['number'] for n in new if n not in old]
        self.deletes = [o['number'] for o in old if o not in new and o['number'] not in self.updates]

        log.info('%d updates to be fetched...' % len(self.updates))
        log.info('%d deletes to be executed...' % len(self.deletes))
        
        # iterate each issue to update or delete
        # only retrive issues that needed to be updated,
        # avoid to request from Github too many times
        for iss in r.json():
            issue = Issue(self.cfg, iss)

            if issue.index in self.deletes:
                issue.delete()
                self.modifications.append(issue.title)
            elif issue.index in self.updates: 
                issue.retrive()
                issue.create_markdown()
                self.modifications.append(issue.title)

        # create local issues data file 
        # This step SHOULD BE placed after filtering all updates
        # means no data will be written into file if there's no updates
        with open(self.cfg.issues_path, 'w') as f:
            f.write(r.text)

        return len(self.modifications)

    def retrive_data(self):
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
            return False

        log.info('Retrived issues successfully. Remaining %s requests limit for this hour.' \
                % r.headers['X-RateLimit-Remaining'])

        return r
    

    def git_update(self):
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


    def first_run(self):
        """
        Download everything if it's the first run.
        """
        if os.path.exists(self.cfg.repo_dir) is False:
            os.makedirs(self.cfg.repo_dir)

        r = self.retrive_data()
        if r is None:
            return 0

        # create local issues data file
        with open(self.cfg.issues_path, 'w') as f:
            f.write(r.text)

        issues = r.json()
        for iss in issues:
            issue = Issue(self.cfg, iss)
            issue.retrive()
            self.modifications.append(issue.title)

        return len(issues)

