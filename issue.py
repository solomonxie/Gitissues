# -*- coding: utf-8 -*-
# Python3. Preferred in pipenv virtual enviroment.

import os # for folder detecting
import json
import requests
import logging

# This project's module
from comment import Comment

log = logging.getLogger('gitissues.issue')

class Issue:
    """
    Description: A class for a single issue, included every property and function for an issue.
    Instance: This class will be instanized when the update() function of Issues class is called.
    Data: All comments of a issue, are stored in 1 single JSON file, 
          which means there's no need to further requests for each comment.
    """

    def __init__(self, config, iss):
        self.cfg = config
        self.title = iss['title']
        self.index = iss['number']
        self.info = iss['body']
        self.url = iss['comments_url']
        self.counts = iss['comments']
        self.data = []
        self.path = '/tmp/issue-%d-comments.json' % (self.index)
        self.markdown = '%s/markdown/issue-%d.md' % (self.cfg.repo_dir, self.index)

    def retrive(self):
        """
        Retrive an specific issue with detailed information
        """
        #import pdb;pdb.set_trace()

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

        # store JSON string 
        self.data = r.text

        # @ create markdown file for retrived issue
        self.create_markdown()

        log.info('Finished fetching for issue-%d[%s] with %d comments' % (self.index,self.title,self.counts))


    def create_markdown(self):
        """
        Description:
            Create an markdown file for this issue and its all comments
        functionallity: 
            Load a JSON file including all comments of an issue, 
            then extract title, date, content etc., to create a markdown file
        """
        # @@ load comments from json data retrived awhile ago
        comments = json.loads(self.data)

        # @@ prepare contents for output markdown file
        header = '# ' + self.title + '\n' + self.info + '\n\n\n'
        bodies = [cm['body'] for cm in comments]
        content = header + '\n\n\n'.join(bodies)

        if os.path.exists(os.path.dirname(self.markdown)) is False:
            os.makedirs(os.path.dirname(self.markdown))

        # @@ output comments into one issue file, named strictly be <ISSUE-INDEX.md>
        with open(self.markdown, 'w') as f:
            f.write(content)

        log.info('Generated markdown file for [%s] at "%s".'%(self.title, self.markdown))


    def delete(self):
        """
        Delete an issue that no longer exists at remote
        """
        log.warn('Failed to delete. Function "delete" has not yet completed.')

