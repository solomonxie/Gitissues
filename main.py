#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
import json
import logging

from issues_fetching import fetch_issues
from repo_mapping import mapping_repo
from remote_syncing import remote_sync


def main():
    """
    CONNECT 3 scripts in a row as a workflow: Fetching -> mapping -> uploading
    """
    logging.basicConfig(filename='./log/log.txt', level=logging.DEBUG, format='\t%(levelname)s:%(asctime)s:\n%(message)s')
    log = logging.getLogger('root')

    #import pdb;pdb.set_trace()

    if len(sys.argv) is 1:
        log.warn('Please indicate the path of config file.')
        return
   
    # @@ load local config file
    with open(sys.argv[1], 'r') as f:
        config = json.loads(f.read())

    log.info('config loaded.')
    return

    # @@ run workflow step-by-step
    fetch_issues(config)
    mapping_repo(config)
    remote_sync(config)



if __name__ == "__main__":

    main()

