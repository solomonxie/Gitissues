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
        # load secret config data (actual content is not in this repo)
        path = './gitissues-config.json'
        if os.path.islink(path) is True:
            path = os.readlink(path)
        with open(path, 'r') as f:
            cfg = json.loads(f.read())

        # github api related configs
        self.target_repo = cfg['target_repo']
        self.auth = cfg['auth']
        # remote storage configs (a different git repo with the original one)
        self.remote_url = cfg['remote']
        # download resources to local drive
        self.root = cfg['root_dir']
        self.repo_dir = cfg['repo_dir']
        self.log_dir = cfg['log_dir']
        self.last_issues_path  = self.repo_dir + '/last_issues_list.csv' 
        # init universial logger for modules
        self.logger_name = name
        self.__define_logger()


    def __define_logger(self):
        """
        Should only be applied in main() function of module.
        For sub modules, could simply use logging.getLogger('...') to get a sub-logger after it's declared in main() function
        """
        logger = logging.getLogger(self.logger_name)
        logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

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
