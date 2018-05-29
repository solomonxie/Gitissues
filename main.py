# -*- coding: utf-8 -*-
# Python3. Preferred in pipenv virtual enviroment.

import os
import sys
import logging
from datetime import date

from config import Config
from issue import Issue
from issues import Issues


def main():
    """
    Main entry of this project.
    Basically just to connect 3 parts in a row as a workflow: Fetching -> mapping -> uploading
    """
    # @@ load local config file
    cfg = Config()

    # get global logger, which was declared in config file
    log = logging.getLogger('gitissues')
    log.info('Start checking with cloud content...')

    #import pdb;pdb.set_trace()

    # Fetch data from cloud & save changes made
    issues = Issues(cfg)
    issues.update()

    # Compose commit message & push changes to remote repository
    if len(issues.modifications) > 0:
        # Notice: data of modification is from json file which is 'Unicode' 
        # and all others are type of `str`, so needs to unify this one to str
        msg = 'Modified ' + ', '.join(issues.modifications).encode('utf-8')
        # run standard git workflow to push updates
        with os.popen('git -C %s add . 2>&1' % cfg.root) as p:
            log.info('GIT ADDED.')
        with os.popen('git -C %s commit -m "%s" 2>&1' % (cfg.root, msg)) as p:
            log.info('GIT COMMIT:\n' + p.read())
        with os.popen('git -C %s push origin master 2>&1' % cfg.root) as p:
            log.info('GIT PUSH:\n' + p.read())

    log.info('Finished for this round check.\n')


if __name__ == "__main__":

    main()

