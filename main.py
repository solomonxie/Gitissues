#!/usr/bin/env python
# -*- coding: utf-8 -*-

from issues_fetching import fetch_issues
from repo_mapping import mapping_repo
from remote_syncing import remote__sync


def main():
    """
    CONNECT 3 scripts in a row as a workflow: Fetching -> mapping -> uploading
    """
    print 'hello'
    
    #import pdb; pdb.set_trace()

    mapping_repo()






if __name__ == "__main__":
    main()
