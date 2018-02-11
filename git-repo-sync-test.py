
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
    repos       = config['repos']
    backup_dir  = config['backup_dir']
    remote_repo = config['remote']['remote_repo']
    remote_url  = config['remote']['remote_url']
    today       = str(date.today())

    # @@ connect, init or clone to a local repo directory
    repo = git.Repo.init(backup_dir)

    # @ check status and commit untracked changes
    if repo.is_dirty() is False :
        repo.git.add('.')
        repo.git.commit(m='Commit before fetching new on [%s]'%today)

    # @ config and connenct with remote
    remote = repo.create_remote(name=remote_repo, url=remote_url)
    remote = repo.remote()

    # @ pull changes from remote and solve conflicts
    remote.pull()
    
    # @ clear all files but ".git", for the next fetching
    #os.system('find %s ! -iname ".git" -delete'%backup_dir)
    os.system('rm -rf %s'%repo)
    

    # @ fetching issues from internet


    # @ commit newly fetched changes to local repo
    repo.git.add('.')
    repo.git.commit(m='Commit newly fetched data on [%s]'%today)

    # @ push to remote repo
    remote.push()



if __name__ == "__main__":
    main()
