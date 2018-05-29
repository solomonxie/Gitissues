# -*- coding: utf-8 -*-
# Python3. Preferred in pipenv virtual enviroment.


import os           # for folder detecting
import json
import requests     # for retrieving web resources
import logging

log = logging.getLogger('gitissues.issue')

class Comment:
    """
    A class for storing & operating comments of an issue
    """

    def __init__(self, config, cmt):
        self.cfg = config
        self.title = cmt['title']
        self.id = cmt['number']
        self.content = cmt['body']
        self.url = cmt['comments_url']
        self.path = '/tmp/comment_%s.json' % (self.id)
        self.mfile = '%s/markdown/comments/comment-%s.md' % (self.cfg.repo_dir, self.id)

    def retrive(self):
        """
        Retrive a comment for detailed information
        """
        #import pdb;pdb.set_trace()

        # @@ retrive comments, @ with response validation 
        try:
            r = requests.get(self.url + self.cfg.auth, timeout=5)
        except Exception as e:
            log.error('An error occured when requesting a comment from Github:\n%s' % str(e))
            return None

        if r.status_code is not 200:
            log.warn('Failed on fetching comment, due to enexpected response: [%s]' \
                    % self.url)
            return False              # if failed one comment, then restart whole process on this issue

        # @ create markdown file for retrived issue
        self.create_markdown(r.content)

        log.info('Finished fetching for issue-%d[%s] with %d comments' % (self.index,self.title,self.counts))


    def create_markdown(self, json_string):
        """
        Create an markdown file for this comment
        """
        if os.path.exists(os.path.dirname(self.mfile)) is False:
            os.makedirs(os.path.dirname(self.mfile))

        # @@ load comments from json data retrived awhile ago
        data = json.loads(json_string)
        # @@ prepare contents for outputting markdown file
        output = '# ' + self.title + '\n' + self.content

        # @@ output comments into one issue file, named strictly be <ISSUE-INDEX.md>
        with open(self.mfile, 'w') as f:
            f.write(output)
            log.info('Generated markdown file for comment [%s] at "%s".'%(self.title, self.mfile))


    def delete(self):
        """
        Delete a comment that no longer exists at remote
        """
        if os.path.exists(self.path) is False:
            log.warn('Can not delete, no such a file %s' % self.path)

        #os.system('rm %s %s' % (self.path, self.mfile))
        #log.info('Deleted comment-%d[%s] and its markdown file.'%(self.id, self.title))
        log.warn('Failed to delete. Function "delete" has not yet completed.')

