# -*- coding: utf-8 -*-

import os
import sys
import logging
from datetime import date

from config import Config
from issue import Issue
from issues import Issues

from repo_mapping import mapping_repo
from remote_syncing import remote_sync


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
    log.info('Start fetching issues from Github...')

    issues = Issues(cfg)
    if os.path.exists(cfg.issues_path) is False:
        os.system('mv %s /tmp' % cfg.repo_dir)      # clear workplace by removing
        issues.first_run()
    else:
        issues.update()

    if len(issues.modifications) > 0:
        mapping_repo(cfg)
        remote_sync(cfg, issues.modifications)

    log.info('Finished for this round check.\n')


if __name__ == "__main__":

    main()

