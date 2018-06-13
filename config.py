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
    def __init__(self):
        with open('/Volumes/SD/Workspace/etc/configs/gitissues-config.json', 'r') as f:
            cfg = json.loads(f.read())
        # github api related configs
        self.user = cfg["fetch"]["user"]
        self.repo = cfg["fetch"]["repo"]
        self.issues_url = cfg["fetch"]["issues_url"]
        self.auth = cfg["fetch"]["auth"]
        # remote storage configs (a different git repo with the original one)
        self.remote_url = cfg["remote"]["ssh"]
        self.remote_user = cfg["remote"]["user"]
        self.email = cfg["remote"]["email"]
        # download resources to local drive
        self.root = cfg["local"]["root_dir"]
        self.repo_dir     = cfg["local"]["repo_dir"]
        self.log_dir = cfg["local"]["log_dir"]
        self.issues_path  = cfg["local"]["issues_path"]
        # init universial logger for modules
        define_logger('gitissues', self.log_dir)


def define_logger(name, path):
    """
    Should only be applied in main() function of module.
    For sub modules, could simply use logging.getLogger('...') to get a sub-logger after it's declared in main() function
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # make log file path
    if os.path.exists(path) is False:
        os.makedirs(path)
    mainfile  = '%s/gitissues.log' % path
    dailyfile = '%s/gitissues%s.log' % (path, date.today())

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
