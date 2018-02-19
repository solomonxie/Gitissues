#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os           # for folder detecting
import requests     # for retrieving web resources
import logging

log = logging.getLogger('gitissues.issue')


class Issue:
    """
    Define an issue object with properties and basic functions
    """

    def __init__(self, config, iss):

        self.config = config
        self.title = iss['title']
        self.index = iss['number']
        self.comments_url = iss['comments_url']
        self.counts = iss['comments']
        self.path = '%s/comments-for-issue-%d.json' % (config.repo_dir, self.index)


    def update(self):
        """

        """
        # @@ fetch comments, @ with response validation 
        r = requests.get(self.comments_url + self.config.auth, timeout=10)
        if r.status_code is not 200:
            log.warn('Failed on fetching issue, due to enexpected response: [%s]' % self.comments_url)
            return False              # if failed one comment, then restart whole process on this issue

        # @@ log comments as original json file, for future restoration or further use
        with open(self.path, 'w') as f:
            f.write(r.content)

        log.info('Fetched for issue-%d[%s] with %d comments' % (self.index,self.title,self.counts))


    def delete(self):
        """

        """
        if os.path.exists(self.path):
            os.system('rm %s'%self.path)
            log.info('Deleted issue-%d[%s].'%(self.index, self.title))

