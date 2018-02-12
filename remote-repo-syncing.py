#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
from datetime import date
import time

import json
import git


def main():

    import pdb; pdb.set_trace()   # debugging mode

    # @@ read config file
    with open('config.json', 'r') as f:
        config = json.loads(f.read())

    # @@ initialize config variables
    fetched_user = config['fetch']['user']
    root         = config['fetch']['root_dir']
    remote_name  = config['remote']['repo']
    remote_url   = config['remote']['ssh']
    today        = str(date.today())

    # @@ connect, init or clone to a local repo directory
    repo = git.Repo.init(root)

    # (Workflow: before download new data, commit local repo first, then pull remote changes, then download new data and push to remote)

    # @ check untracked files and commit 
    os.system('git add .')
    os.system('git commit -m "Commit before fetching new on [%s]"'%today)
    #for u in repo.untracked_files:
    #if repo.is_dirty():
    #    repo.git.add('.')
    #    repo.git.commit(m='Commit before fetching new on [%s]'%today)

    # @ setup remote address and authentication
    os.system('')
    os.system('')
    os.system('')
    #remote = repo.create_remote(name=remote_name, url=remote_url)
    #remote = repo.remote()

    # @ pull changes from remote and solve conflicts
    os.system('git pull')
    #remote.pull()
    
    # @ clear directory before download new data. Not blindly remove everything but only remove repos will be renewed
    shutil.rmtree(root+'/'+fetched_user)
    

    # @ fetching issues from internet


    # @ mapping json dato to markdown files


    # @ commit newly fetched changes to local repo
    os.system('git add .')
    os.system('git commit -m "Commit newly fetched data on [%s]"'%today)
    #repo.git.add('.')
    #repo.git.commit(m='Commit newly fetched data on [%s]'%today)

    # @ push to remote repo
    os.system('git push')
    #remote.push()



if __name__ == "__main__":
    main()
