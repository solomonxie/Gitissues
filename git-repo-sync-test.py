
import shutil
from datetime import date

import json
import git


def main():

    import pdb; pdb.set_trace()   # debugging mode

    # @@ read config file
    with open('config.json', 'r') as f:
        config = json.loads(f.read())

    # @@ initialize config variables
    repos       = config['fetch']['repos']
    root        = config['fetch']['root_dir']
    remote_name = config['remote']['repo']
    remote_url  = config['remote']['ssh']
    today       = str(date.today())

    # @@ connect, init or clone to a local repo directory
    repo = git.Repo.init(root)

    # @ check untracked files and commit 
    #for u in repo.untracked_files:
    if repo.is_dirty():
        repo.git.add('.')
        repo.git.commit(m='Commit before fetching new on [%s]'%today)

    # @ config and connenct with remote
    remote = repo.create_remote(name=remote_name, url=remote_url)
    remote = repo.remote()

    # @ pull changes from remote and solve conflicts
    remote.pull()
    
    # @ not blindly remove everything but only remove repos will be renewed
    

    # @ fetching issues from internet


    # @ commit newly fetched changes to local repo
    repo.git.add('.')
    repo.git.commit(m='Commit newly fetched data on [%s]'%today)

    # @ push to remote repo
    remote.push()



if __name__ == "__main__":
    main()
