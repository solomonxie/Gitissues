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



def remote_sync():
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
    remote_url   = config['remote']['https']
    email        = config['remote']['email']
    today        = str(date.today())

    # @@ connect, init or clone to a local repo directory
    repo = git.Repo.init(root)
    print 'git repo created: %s'%root

    import pdb; pdb.set_trace()   # debugging mode

    # @@ check untracked files and commit 
    #if repo.is_dirty():
    repo.git.add('.')
    try:
        repo.git.commit(m='Fetched on [%s]'%today)
        print 'change committed.'
    except: pass

    # @@ run script to make a `.git/config` file
    with open('sample-git-config', 'r') as f:
        git_config = f.read()

    with open(root+'/.git/config', 'rw') as f:
        if len(f.read()) is 0:
            f.write(git_config.format(remote_url=remote_url, email=email))


    # @@ setup remote connection
    remote = repo.remote()

    # @@ pull changes from remote and solve conflicts
    remote.fetch()
    print 'fetched.'
    #remote.pull()
    #print 'pulled.'
    
    # @@ push to remote repo
    remote.push() 
    print 'pushed.'


if __name__ == "__main__":
    main()
