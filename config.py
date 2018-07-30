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

log = None

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
        self.target_url = f'https://api.github.com/repos/{self.target_user}/{self.target_repo}/issues'
        self.auth = cfg['auth']

        # Remote backup repo (where we're gonna store all fetched contents)
        self.backup_url = cfg['backup_url']
        # Local repo (Regards to the Remote backup repo)
        self.backup_dir = cfg['backup_local_repo']

        # Logging path
        self.log_dir = f'{self.backup_dir}/.local/log'
        if os.path.exists(self.log_dir) is not True:
            os.makedirs(self.log_dir)
        # Global logger for all modules
        self.log = self.__define_logger('gitissues')


        _target = f'[{self.target_user}][{self.target_repo}]'
        # Issues path
        self.issues_api = self.target_url + self.auth
        self.issues_raw_path = f'{self.backup_dir}/.local/{_target}/last_issues_list.json'
        self.last_issues_list_path  = f'{self.backup_dir}/.local/{_target}/last_issues_list.csv'

        # Issue path
        self.issue_dir = f'{self.backup_dir}/docs-{_target}/issue-' +'{}'
        self.issue_raw = f'{self.backup_dir}/.local/{_target}/issue-' +'{}.json'
        self.issue_csv = f'{self.backup_dir}/.local/{_target}/issue-' +'{}.csv'


        # Comment path
    

    def __init_paths(self):
        """ Initialize all paths """
        pass

    def request_url(self, url):
        try:
            r = requests.get(url, timeout=5)

        except Exception as e:
            log.error(f'An error occured when requesting:\n{str(e)}')
            log.error('Mission aborted.')
            return None

        if r.status_code is not 200:
            log.error(f'Failed on fetching {url} due to unexpected response')
            __limit = r.headers['X-RateLimit-Remaining']
            log.debug(f'Remain {__limit} requests limit in this hour.')
            return None
        
        return r

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
        last_log = f'{self.log_dir}/last.log'
        daily_log = f'{self.log_dir}/{logger_name}-{date.today()}.log'

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
