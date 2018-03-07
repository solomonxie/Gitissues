# -*- coding: utf-8 -*-

import os
import sys
import logging
from datetime import date

class Config:
    """
    Loading settings from customized configs (json)
    """
    def __init__(self):
        self.user         = "solomonxie"
        self.repo         = "solomonxie.github.io"
        self.issues_url   = "https://api.github.com/repos/solomonxie/solomonxie.github.io/issues"
        #self.auth         = "?client_id=????&client_secret=????"
        self.auth_file    = "/Volumes/SD/Workspace/etc/github-auth-client.txt"
        self.remote_url   = "git@github.com:solomonxie/user_content_issues_blog.git"
        self.remote_user  = "Solomon Xie"
        self.email        = "solomonxiewise@gmail.com"
        self.root         = "/Volumes/SD/Workspace/autobackup/user_content_issues_blog"
        self.repo_dir     = "%s/%s/%s" % (self.root, self.user, self.repo)
        self.issues_path  = self.repo_dir + '/issues.json'
        self.log_dir      = "/Volumes/SD/Workspace/autobackup/logs/gitissues"

        # init universial logger for modules
        define_logger('gitissues', self.log_dir)

        # read auth string from a local file outside of public repository
        with open(self.auth_file, 'r') as f:
            self.auth = f.read().strip()


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
