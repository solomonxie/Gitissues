#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging


def remote_sync(config):
    """
    Push newly fetched data to remote repository
    """
    # run standard git workflow to push updates
    os.system('git -C %s add .'%(config.root))
    os.system('git -C %s commit -m "Update from `uname -n`"'%(config.root))
    #os.system('git -C %s pull --rebase origin master'%(config.root))       # rebase
    os.system('git -C %s push origin master'%(config.root))

