# -*- coding: utf-8 -*-

import os
import logging

from config import Config


def remote_sync(config, modifications=[]):
    """
    Push newly fetched data to remote repository
    """
    #import pdb;pdb.set_trace()
    log = logging.getLogger('gitissues.remote_syncing')
    cwd = config.root

    # Notice: data of modification is from json file which is 'Unicode' 
    # and all others are type of `str`, so needs to unify this one to str
    msg = 'Modified ' + ', '.join(modifications).encode('utf-8')          #msg = '`uname -n`'
    
    # run standard git workflow to push updates
    os.system('git -C %s add .' % cwd)
    with os.popen('git -C %s commit -m "%s" 2>&1' % (cwd, msg)) as p:
        log.info('\n' + p.read())
    with os.popen('git -C %s push origin master 2>&1' % cwd) as p:
        log.info('\n' + p.read())


if __name__ == "__main__":
    # testing
    cfg = Config()
    mods = [u'Python学习笔记']
    remote_sync(cfg, mods)
