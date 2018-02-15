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

    #import pdb;pdb.set_trace()

    # @@ load local config file
    with open('config.json', 'r') as f:
        config = json.loads(f.read())


    # @@ run workflow step-by-step
    fetch_issues(config)
    mapping_repo(config)
    remote_sync(config)



if __name__ == "__main__":

    #main()

    while True:
        try:
            main()
            print('It will run again in 1 minutes...')
            time.sleep(60)
        except Exception as e:
            print(e.message)

