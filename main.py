# -*- coding: utf-8 -*-
# ==== This project is required to work in Python2 enviroment, preferred Virtualenv enviroment. ====

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
    #import pdb;pdb.set_trace()

    # @@ load local config file
    cfg = Config()

    # get global logger, which was declared in config file
    log = logging.getLogger('gitissues')
    log.info('Start checking with cloud content...')

    # Fetch data from cloud & save changes made
    issues = Issues(cfg)
    # Sync with cloud before any changes
    issues.git_update()
    if os.path.exists(cfg.issues_path) is False:
        os.system('mv %s /tmp' % cfg.repo_dir)      # clear workplace by removing
        issues.first_run()
    else:
        issues.update()

    # Push changes to remote repository
    if len(issues.modifications) > 0:
        # Notice: data of modification is from json file which is 'Unicode' 
        # and all others are type of `str`, so needs to unify this one to str
        msg = 'Modified ' + ', '.join(issues.modifications).encode('utf-8')          #msg = '`uname -n`'
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

