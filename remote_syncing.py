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
    try:
        repo = git.Repo(root)

    except:
        # @@ run script to make a `.git/config` file
        with open('sample-git-config', 'r') as f:
            git_config = f.read()
        with open(root+'/.git/config', 'rw') as f:
            if len(f.read()) is 0:
                f.write(git_config.format(remote_url=remote_url, email=email))

        print 'Please manually setup remote config in: %s\n\
                A sample git config has copied to ".git/config"'%root
        return 

    print 'git repo connected: %s'%root


    #import pdb; pdb.set_trace()   # debugging mode

    # @@ check untracked files and commit 
    #if repo.is_dirty():
    repo.git.add('.')
    try:
        repo.git.commit(m='Fetched on [%s]'%today)
        print 'change committed.'
    except:
        print 'Commit failed. Please manually set up git config for further operation.'
        return


    # @@ setup remote connection
    remote = repo.remote()

    # @@ fetch, pull and push with remote
    try:
        remote.fetch()
        print 'fetched.'
        remote.pull()
        print 'pulled.'
        remote.push() 
        print 'pushed.'
    except:
        print 'Communicate with failed. Please manually set up git config for further operation.'
        return


if __name__ == "__main__":
    main()
