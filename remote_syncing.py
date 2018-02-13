#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
from datetime import date
import time

import json
import git


def main():

    remote_sync()



def remote__sync():
    """
    Push newly fetched data to remote repository
    """

    #import pdb; pdb.set_trace()   # debugging mode

    # @@ read config file
    with open('config.json', 'r') as f:
        config = json.loads(f.read())

    # @@ load config variables 
    fetched_user = config['fetch']['user']
    root         = config['local']['root_dir']
    today        = str(date.today())

    # @@ connect, init or clone to a local repo directory
    repo = git.Repo.init(root)

    #import pdb; pdb.set_trace()   # debugging mode

    # @@ check untracked files and commit 
    if repo.is_dirty():
        print repo.git.add('.')
        print repo.git.commit(m='Commit before fetching new on [%s]'%today)

    # @@ setup remote connection
    remote = repo.remote()

    # @@ pull changes from remote and solve conflicts
    remote.pull()
    
    # @@ push to remote repo
    remote.push() 


if __name__ == "__main__":
    main()
