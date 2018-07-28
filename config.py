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

class Config:
    """
    Loading settings from customized configs (json)
    """
    def __init__(self, name):
        # Create local folders for storing data
        if os.path.exists('./.local/log') is not True:
            os.makedirs('./.local/log')

        # Load local secret config data (actual content is not in this repo)
        path = '.local/gitissues-config.json'
        with open(path, 'r') as f:
            cfg = json.loads(f.read())

        # Logging path
        self.log_dir = './.local/log'
        # Global logger for all modules
        self.logger_name = name
        self.__define_logger()

        # Target Github repo (where we're gonna be fetching)
        self.target_user = cfg['target_user']
        self.target_repo = cfg['target_repo']
        self.target_url = f'https://api.github.com/repos/{self.target_user}/{self.target_repo}/issues'
        self.auth = cfg['auth']

        # Remote backup repo (where we're gonna store all fetched contents)
        self.backup_url = cfg['backup_url']
        # Local repo (Regards to the Remote backup repo)
        self.backup_dir = cfg['backup_local_repo']




    def __define_logger(self):
        """
        Should only be applied in main() function of module.
        For sub modules, could simply use logging.getLogger('...') to get a sub-logger after it's declared in main() function
        """
        logger = logging.getLogger(self.logger_name)
        logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter('\n%(asctime)s - %(name)s - %(levelname)s :\n\n\t%(message)s')

        # make log file path
        if os.path.exists(self.log_dir) is False:
            os.makedirs(self.log_dir)
        mainfile  = '%s/last.log' % self.log_dir
        mainfile = f'{self.log_dir}/last.log'
        dailyfile = f'{self.log_dir}/{self.logger_name}-{date.today()}.log'

        # create a file handler for logging
        main = logging.FileHandler(mainfile, mode='w')
        main.setFormatter(formatter)
        daily = logging.FileHandler(dailyfile)
        daily.setFormatter(formatter)

        # create a stream(stdout) handler for logging
        screen  = logging.StreamHandler(stream=None)
        screen.setFormatter(formatter)

        # add handlers to logger object
        logger.addHandler(main)
        logger.addHandler(daily)
        logger.addHandler(screen)

        return logger
