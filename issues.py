#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os           # for folder detecting
import json
import requests     # for retrieving web resources
import logging

from issue import Issue

log = logging.getLogger('gitissues.issues')


class Issues:
    """
    Handling updating/deleting/creating issues-list
    The core part of this project.
    """
    def __init__(self, config):
        self.config = config
        self.updates = []
        self.deletes = []
        self.issues = []


    def retrive_data(self):
        """
        Retrieving data from internet, @ with response validation
        """
        log.info('Now retriving [%s]...' \
                % (self.config.issues_url + self.config.auth))

        r = requests.get(self.config.issues_url + self.config.auth, timeout=10)

        if r.status_code is not 200:
            log.warn('Failed on fetching [%s] due to unexpected response' \
                    % self.config.issues_url)
            return False

        log.debug('Remaining %s requests limit for this hour.' \
                % r.headers['X-RateLimit-Remaining'])

        return r
    

    def git_update(self):
        """
        Need to prepare local user content repository always updated with remote before make any change
        Just for avoiding conflict
        """
        # @@ prepare local git repo for the first time
        if os.path.exists(self.config.root) is False:
            log.debug('local repo does not exist, setting up now...')
            with os.popen('git clone %s %s 2>&1' % (self.config.remote_url, self.config.root)) as p:
                log.info(p.read())

        # @ keep local repo updated with remote before further change to avoid conflict
        log.info('Check git remote status before further updates: ')
        with os.popen('git -C %s pull 2>&1' % (self.config.root)) as p:
            log.info(p.read())

        # @@ setup default configuration
        os.system('git -C %s config credential.helper cache'%self.config.root)
        os.system('git -C %s config user.email %s'%(self.config.root, self.config.email))
        os.system('git -C %s config user.name %s'%(self.config.root, self.config.remote_user))


    def first_run(self):
        """
        Download everything if it's the first run.
        """
        self.git_update()
        r = self.retrive_data()

        issues = r.json()
        for iss in issues:
            issue = Issue(self.config, iss)
            issue.update()

        return len(issues)


    def update(self):
        """
        Update local stored issues data
        Introduced filtering algorithm to avoid updating a non-changed content
        """
        self.git_update()
        r = self.retrive_data()

        log.info('Filtering updated and deleted items...')
        # @@ match updated issues and deleted items
        with open(self.config.issues_path, 'r') as f:
            new = r.json()
            old = json.loads(f.read())

        # @@ filter out same issues from deletes that also exist in updates
        self.updates = [n['number'] for n in new if n not in old]
        self.deletes = [o['number'] for o in old if o not in new and o['number'] not in self.updates]

        log.info('%d updates to be fetched...' % len(self.updates))
        log.info('%d deletes to be executed...' % len(self.deletes))
        
        # iterate each issue for operation
        for iss in r.json():
            issue = Issue(self.config, iss)
            if issue.index in self.deletes:
                issue.delete()
            elif issue.index in self.updates: 
                issue.update()

        # update local issues data file
        with open(self.config.issues_path, 'w') as f:
            f.write(r.content)

        return len(self.updates)

