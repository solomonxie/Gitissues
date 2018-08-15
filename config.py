# -*- coding: utf-8 -*-
# Python3. Preferred in pipenv virtual enviroment.

"""
File: config.py
Author: Solomon Xie
Email: solomonxiewise@gmail.com
Github: https://github.com/solomonxie
Description: 
    How this module works:
"""

import os
import sys
import logging
import json
from datetime import date

import requests


class Config:
    """
    Loading settings from customized configs (json)
    """
    def __init__(self, cfg_path):
        # Load local secret config data (actual content is not in this repo)
        with open(cfg_path, 'r') as f:
            cfg = json.loads(f.read())
        
        self.cwd = os.getcwd()

        # Target Github repo (where we're gonna be fetching)
        self.target_user = cfg['target_user']
        self.target_repo = cfg['target_repo']
        self.target_url = 'https://api.github.com/repos/{}/{}/issues'.format( \
                            self.target_user, self.target_repo)
        self.auth = cfg['auth']

        # Remote backup repo (where we're gonna store all fetched contents)
        self.backup_url = cfg['backup_url']
        # Local repo (Regards to the Remote backup repo)
        self.backup_dir = cfg['backup_local_repo']

        # Logging path
        self.log_dir = '{}/.local/log'.format(self.backup_dir)
        if os.path.exists(self.log_dir) is not True:
            os.makedirs(self.log_dir)
        # Global logger for all modules
        self.log = self.__define_logger('gitissues')


        _target = '[{}][{}]'.format(self.target_user, self.target_repo)
        self.target = _target

        # Issues path
        self.issues_api = self.target_url + self.auth
        self.issues_raw_path = '{}/.local/{}/last_issues_list.json'.format(self.backup_dir, _target)
        self.last_issues_list_path  = '{}/.local/{}/last_issues_list.csv'.format(self.backup_dir, _target)
    

    def get_path_issue_dir(self, index):
        return '{}/docs-{}/issue-{}'.format(self.backup_dir, self.target, index)
    
    def get_path_issue_raw(self, index):
        return '{}/.local/{}/issue-{}.json'.format(self.backup_dir, self.target, index)
    
    def get_path_issue_csv(self, index):
        return '{}/.local/{}/issue-{}.csv'.format(self.backup_dir, self.target, index)
        
    def get_path_issue_markdown(self, index):
        return '{}/issue-{}.md'.format(self.get_path_issue_dir(index), index)

    def get_path_issue_html(self, index):
        return '{}/issue-{}.html'.format(self.get_path_issue_dir(index), index)
    
    def get_path_issue_review_dates_csv(self, index):
        return '{}/.local/{}/issue-{}-review.csv'.format(self.backup_dir, self.target, index)

    def request_url(self, url):
        try:
            r = requests.get(url, timeout=5)

        except Exception as e:
            self.log.error(e)
            self.log.error('Mission aborted.\nAn error occured when requesting:\n%s\n'%url)
            return None

        if r.status_code is not 200:
            self.log.error('Failed on fetching %s due to unexpected response'%url)
            return None
        
        __limit = r.headers['X-RateLimit-Remaining']
        self.log.info('Remain %s requests limit in this hour.'%__limit)
        return r

    def __init_paths(self):
        """ Initialize all paths """
        pass

    def __define_logger(self, logger_name):
        """
        Should only be applied in main() function of module.
        For sub modules, could simply use logging.getLogger('...') to get a sub-logger after it's declared in main() function
        """
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter('\n%(asctime)s - %(name)s - %(levelname)s :\n\n\t%(message)s')

        # make log file path
        if os.path.exists(self.log_dir) is False:
            os.makedirs(self.log_dir)
        last_log = '%s/last.log'%self.log_dir
        daily_log = '{}/{}-{}.log'.format(self.log_dir, logger_name, date.today())

        # create a file handler for logging
        main = logging.FileHandler(last_log, mode='w')
        main.setFormatter(formatter)
        daily = logging.FileHandler(daily_log)
        daily.setFormatter(formatter)

        # create a stream(stdout) handler for logging
        screen  = logging.StreamHandler(stream=None)
        screen.setFormatter(formatter)

        # add handlers to logger object
        logger.addHandler(main)
        logger.addHandler(daily)
        logger.addHandler(screen)

        return logger
