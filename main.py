#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import logging

from issue import Issue
from issues import Issues
from config import Config

from repo_mapping import mapping_repo
from remote_syncing import remote_sync


def main():
    """
    CONNECT 3 scripts in a row as a workflow: Fetching -> mapping -> uploading
    """

    #import pdb;pdb.set_trace()

    # @@ load local config file
    path = os.path.dirname(os.path.realpath(sys.argv[0])) + '/config.json'
    config = Config(path)

    issues = Issues(config)

    if os.path.exists(config.issues_path) is False:
        os.system('rm -rf %s' % config.repo_dir)
        issues.first_run()
    else:
        tasks = issues.update()
        if tasks > 0:
            mapping_repo(config)
            remote_sync(config)



if __name__ == "__main__":

    main()

