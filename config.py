#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

class Config:
    """
    Loading settings from customized configs (json)
    """
    def __init__(self):
        self.user         = "solomonxie"
        self.repo         = "solomonxie.github.io"
        self.issues_url   = "https://api.github.com/repos/solomonxie/solomonxie.github.io/issues"
        self.auth         = "?client_id=0c08b801005ee3005ded&client_secret=da1a866f28556cc27e6ee12ca7c07c35bb548e5b"
        self.remote_url   = "https://github.com/solomonxie/user_content_issues_blog.git"
        self.remote_user  = "Solomon Xie"
        self.email        = "solomonxiewise@gmail.com"
        self.root         = "/Volumes/SD/Workspace/autobackup/user_content_issues_blog"
        self.repo_dir     = "%s/%s/%s" % (self.root, self.user, self.repo)
        self.issues_path  = self.repo_dir + '/issues.json'
        self.log          = "/Volumes/SD/Workspace/autobackup/user_content_issues_blog/solomonxie/gitissues.log"
