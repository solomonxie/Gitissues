#!/usr/bin/env python
# -*- coding: utf-8 -*-

from issues_fetching import fetch_issues
from repo_mapping import mapping_repo
from remote_syncing import remote_sync


def main():
    """
    CONNECT 3 scripts in a row as a workflow: Fetching -> mapping -> uploading
    """
    
    #import pdb; pdb.set_trace()

    fetch_issues()
    mapping_repo()
    remote_sync()






if __name__ == "__main__":
    main()
