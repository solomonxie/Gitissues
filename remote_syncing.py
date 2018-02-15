#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import json


def main():

    # @@ load local config file
    with open('config.json', 'r') as f:
        config = json.loads(f.read())

    remote_sync(config)


def remote_sync(config):
    """
    Push newly fetched data to remote repository
    """

    #import pdb; pdb.set_trace()   # debugging mode

    root = config['local']['root_dir']

    # run standard git workflow to push updates
    os.system('git -C %s add .'%(root))
    os.system('git -C %s commit -m "Update at `date`"'%(root))
    os.system('git -C %s pull --rebase origin master'%(root))       # rebase
    os.system('git -C %s push origin master'%(root))




if __name__ == "__main__":
    main()
