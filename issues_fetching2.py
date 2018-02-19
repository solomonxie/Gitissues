#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os           # for folder detecting
import sys
import json
import shutil       # for zipping files
import requests     # for retrieving web resources
import logging
import time
from datetime import date



def main():

    #import pdb; pdb.set_trace()

    # @@ load local config file
    path = os.path.dirname(os.path.realpath(sys.argv[0])) + '/config.json'
    config = Config(path)

    issues = Issues(config)

    if os.path.exists(config.repo_dir+'/issues.json') is False:
        os.system('rm -rf %s' % config.repo_dir)
        issues.first_run()
    else:
        issues.update()


class Issue:
    """
    Define an issue object with properties and basic functions
    """

    def __init__(self, config, iss):

        self.config = config
        self.title = iss['title']
        self.index = iss['number']
        self.comments_url = iss['comments_url']
        self.counts = iss['comments']
        self.path = '%s/comments-for-issue-%d.json' % (config.repo_dir, self.index)


    def update(self):
        """

        """
        # @@ fetch comments, @ with response validation 
        r = requests.get(self.comments_url + self.config.auth, timeout=10)
        if r.status_code is not 200:
            print('Failed on fetching issue, due to enexpected response: [%s]' % self.comments_url)
            return False              # if failed one comment, then restart whole process on this issue

        # @@ log comments as original json file, for future restoration or further use
        with open(self.path, 'w') as f:
            f.write(r.content)

        print('Fetched for issue-%d[%s] with %d comments' % (self.index,self.title,self.counts))


    def delete(self):
        """

        """
        if os.path.exists(self.path):
            os.system('rm %s'%self.path)
            print('Deleted issue-%d[%s].'%(self.index, self.title))



class Config:
    """
    Loading settings from customized configs (json)
    """
    def __init__(self, path):
        # @@ loading settings from customized configs (json)
        with open(path, 'r') as f:
            cfg = json.loads(f.read())

        self.user         = cfg['fetch']['user']
        self.repo         = cfg['fetch']['repo']
        self.issues_url   = cfg['fetch']['issues_url']
        self.auth         = cfg['fetch']['auth2_ks']
        self.remote_url   = cfg['remote']['https']
        self.remote_user  = cfg['remote']['user']
        self.email        = cfg['remote']['email']
        self.root         = cfg['local']['root_dir']
        self.repo_dir     = '%s/%s/%s' % (self.root, self.user, self.repo)



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
        with open(self.config.repo_dir+'/issues.json', 'r') as f:
            new = r.json()
            old = json.loads(f.read())

        # !@ filter out same issues from deletes that also exist in updates
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

        return len(self.updates)



if __name__ == "__main__":
    main()
