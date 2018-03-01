# -*- coding: utf-8 -*-

import os           # for folder detecting
import requests     # for retrieving web resources
import logging

log = logging.getLogger('gitissues.issue')


class Issue:
    """
    A class for a single issue, included every property and function for an issue.
    """

    def __init__(self, config, iss):

        self.config = config
        self.title = iss['title']
        self.index = iss['number']
        self.comments_url = iss['comments_url']
        self.counts = iss['comments']
        self.path = '%s/comments-for-issue-%d.json' % (config.repo_dir, self.index)


    def retrive(self):
        """
        Retrive an specific issue with detailed information
        """
        # @@ retrive comments, @ with response validation 
        try:
            r = requests.get(self.comments_url + self.config.auth, timeout=5)
        except Exception as e:
            log.error('An error occured when requesting from Github:\n%s' % str(e))
            log.info('Mission aborted.')
            return None

        if r.status_code is not 200:
            log.warn('Failed on fetching issue, due to enexpected response: [%s]' \
                    % self.comments_url)
            return False              # if failed one comment, then restart whole process on this issue

        # @@ log comments as original json file, for future restoration or further use
        with open(self.path, 'w') as f:
            f.write(r.content)

        log.info('Fetched for issue-%d[%s] with %d comments' % (self.index,self.title,self.counts))


    def delete(self):
        """
        Delete an issue that no longer exists at remote
        """
        if os.path.exists(self.path):
            os.system('rm %s'%self.path)
            log.info('Deleted issue-%d[%s].'%(self.index, self.title))

