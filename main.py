#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
import json

from issues_fetching import fetch_issues
from repo_mapping import mapping_repo
from remote_syncing import remote_sync


def main():
    """
    CONNECT 3 scripts in a row as a workflow: Fetching -> mapping -> uploading
    """

    #import pdb;pdb.set_trace()

    if len(sys.argv) is 1:
        print 'Please indicate the path of config file.'
        return
   
    # @@ load local config file
    with open(sys.argv[1], 'r') as f:
        config = json.loads(f.read())

    # @@ run workflow step-by-step
    fetch_issues(config)
    mapping_repo(config)
    remote_sync(config)



if __name__ == "__main__":

    main()

    # @@ run script for every 5 minutes
    #while True:
    #    try:
    #        main()

    #    except Exception as e:
    #        print e.message
    #        continue

    #    time.sleep(5*60)
