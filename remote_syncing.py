#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging


def remote_sync(config):
    """
    Push newly fetched data to remote repository
    """
    log = logging.getLogger('gitissues.remote_syncing')

    cwd = config.root
    # run standard git workflow to push updates
    os.system('git -C %s add .' % cwd)
    with os.popen('git -C %s commit -m "Update from `uname -n`" 2>&1' % cwd) as p:
        log.info('\n' + p.read())
    with os.popen('git -C %s push origin master 2>&1' % cwd) as p:
        log.info('\n' + p.read())

