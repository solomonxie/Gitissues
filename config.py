#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import logging


class Config:
    """
    Loading settings from customized configs (json)
    """
    def __init__(self, path):
        # @@ loading settings from customized configs (json)
        with open(path, 'r') as f:
            cfg = json.loads(f.read())

        self.user         = cfg['fetch']['user']
        self.repo         = cfg['fetch']['repo']
        self.issues_url   = cfg['fetch']['issues_url']
        self.auth         = cfg['fetch']['auth2_ks']
        self.remote_url   = cfg['remote']['https']
        self.remote_user  = cfg['remote']['user']
        self.email        = cfg['remote']['email']
        self.root         = cfg['local']['root_dir']
        self.repo_dir     = '%s/%s/%s' % (self.root, self.user, self.repo)
        self.issues_path  = self.repo_dir + '/issues.json'
