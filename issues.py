#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os           # for folder detecting
import json
import requests     # for retrieving web resources
import logging

from issue import Issue


class Issues:
    """

    """
    def __init__(self, config):
        self.config = config
        self.updates = []
        self.deletes = []
        self.issues = []
        self.updatodate = True


    def retrive_data(self):
        """
        Retrieving data from internet, @ with response validation
        """
        print('Now retriving [%s]...' \
                % (self.config.issues_url + self.config.auth))

        r = requests.get(self.config.issues_url + self.config.auth, timeout=10)

        if r.status_code is not 200:
            print('Failed on fetching [%s] due to unexpected response' \
                    % self.config.issues_url)
            return False

        print('Remaining %s requests limit for this hour.' \
                % r.headers['X-RateLimit-Remaining'])

        return r
    

    def git_update(self):
        # @@ prepare local git repo for the first time
        if os.path.exists(self.config.root) is False:
            print('local repo does not exist, setting up now...')
            os.system('git clone %s %s'%(self.config.remote_url, self.config.root))

        # @ keep local repo updated with remote before further change to avoid conflict
        print('Git pull and Git config,  before further updates: ')
        os.system('git -C %s pull'%self.config.root)

        # @@ setup default configuration
        os.system('git -C %s config credential.helper cache'%self.config.root)
        os.system('git -C %s config user.email %s'%(self.config.root, self.config.email))
        os.system('git -C %s config user.name %s'%(self.config.root, self.config.remote_user))


    def first_run(self):
        """

        """
        self.git_update()
        r = self.retrive_data()

        issues = r.json()
        for iss in issues:
            issue = Issue(config, iss)
            issue.update()

        return len(issues)


    def update(self):
        """

        """
        self.git_update()
        r = self.retrive_data()

        print('Filtering updated and deleted items...')
        # @@ match updated issues and deleted items
        with open(self.config.issues_path, 'r') as f:
            new = r.json()
            old = json.loads(f.read())

        # @@ filter out same issues from deletes that also exist in updates
        self.updates = [n['number'] for n in new if n not in old]
        self.deletes = [o['number'] for o in old if o not in new and o['number'] not in self.updates]

        print('%d updates to be fetched...\n%d deletes to be executed...' \
                % (len(self.updates), len(self.deletes)))
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

