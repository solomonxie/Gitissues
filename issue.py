# -*- coding: utf-8 -*-
# ==== This project is required to work in Python2 enviroment, preferred Virtualenv enviroment. ====

import os           # for folder detecting
import json
import requests     # for retrieving web resources
import logging

log = logging.getLogger('gitissues.issue')


class Issue:
    """
    A class for a single issue, included every property and function for an issue.
    """

    def __init__(self, config, iss):

        self.cfg = config
        self.title = iss['title']
        self.index = iss['number']
        self.info = iss['body']
        self.url = iss['comments_url']
        self.counts = iss['comments']
        self.path = '/tmp/issue-%d-comments.json' % (self.index)
        self.markdown = '%s/markdown/issue-%d.md' % (self.cfg.repo_dir, self.index)

    def retrive(self):
        """
        Retrive an specific issue with detailed information
        """
        # @@ retrive comments, @ with response validation 
        try:
            r = requests.get(self.url + self.cfg.auth, timeout=5)
        except Exception as e:
            log.error('An error occured when requesting from Github:\n%s' % str(e))
            log.info('Mission aborted.')
            return None

        if r.status_code is not 200:
            log.warn('Failed on fetching issue, due to enexpected response: [%s]' \
                    % self.url)
            return False              # if failed one comment, then restart whole process on this issue

        # @@ log comments as original json file, for future restoration or further use
        #with open(self.path, 'w') as f:
        #    f.write(r.content)

        # @ create markdown file for retrived issue
        self.create_markdown()

        log.info('Fetched for issue-%d[%s] with %d comments' % (self.index,self.title,self.counts))


    def delete(self):
        """
        Delete an issue that no longer exists at remote
        """
        if os.path.exists(self.path) is False:
            log.warn('Can not delete, no such a file %s' % self.path)

        #os.system('rm %s %s' % (self.path, self.markdown))
        #log.info('Deleted issue-%d[%s] and its markdown file.'%(self.index, self.title))
        log.warn('Failed to delete. Function "delete" has not yet completed.')


    def create_markdown(self):
        """
        Create an markdown file for this issue and its all comments
        """
        # @@ load comments
        with open(self.path, 'r') as f:
            comments = json.loads(f.read())

        # @@ prepare contents for output markdown file
        header = '# ' + self.title + '\n' + self.info + '\n\n\n'
        bodies = [cm['body'] for cm in comments]
        content = header + '\n\n\n'.join(bodies)

        if os.path.exists(os.path.dirname(self.markdown)) is False:
            os.makedirs(os.path.dirname(self.markdown))

        # @@ output comments into one issue file, named strictly be <ISSUE-INDEX.md>
        with open(self.markdown, 'w') as f:
            f.write(content.encode('utf-8'))

        log.info('Generated markdown file for %s at %s.'%(self.title, self.markdown))

