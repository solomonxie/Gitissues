#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

from issues_fetching import fetch_issues
from repo_mapping import mapping_repo
from remote_syncing import remote_sync


def main(auth):
    """
    CONNECT 3 scripts in a row as a workflow: Fetching -> mapping -> uploading
    """
   
    # @@ load local config file
    with open('/Volumes/SD/Workspace/etc/gitissues-config.json', 'r') as f:
        config = json.loads(f.read())

    # @@ run workflow
    fetch_issues(config)
    mapping_repo(config)
    remote_sync(config)



if __name__ == "__main__":

    import pdb; pdb.set_trace()


    #main(auth)

    import requests
    r = requests.get('https://api.github.com/repos/solomonxie/solomonxie.github.io/issues'+auth)
    print r.status_code
    print r.headers['X-RateLimit-Remaining']

    # @@ run script for every 5 minutes
    #while True:
    #    try:
    #        main(auth)

    #    except Exception as e:
    #        print e.message
    #        continue

    #    time.sleep(5)
