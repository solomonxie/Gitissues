# -*- coding: utf-8 -*-
# Python3. Preferred in virtual enviroment.

"""
File: main.py
Author: Solomon Xie
Email: solomonxiewise@gmail.com
Github: https://github.com/solomonxie
Description: 
"""


import os
import sys
import logging
from datetime import date

# This project's module
from config import Config
from issue import Issue
from issues import Issues
from comment import Comment


def main():
    """
    Main entry of this project.
    Basically just to connect 3 parts in a row as a workflow: Fetching -> mapping -> uploading
    """

    # @@ load local config file
    cfg = Config('gitissues')

    # get global logger, which was declared in config file
    log = logging.getLogger('gitissues')
    log.info('Start checking with cloud content...')

    # Fetch data from cloud & save changes made
    issues = Issues(cfg)
    issues.git_pull()
    import pdb;pdb.set_trace()
    issues.update()
    issues.git_push()

    log.info('Finished for this round check.\n')


if __name__ == "__main__":

    main()

