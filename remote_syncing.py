#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json


def main():

    if len(sys.argv) is 1:
        print 'Please indicate the path of config file.'
        return

    # @@ load local config file
    with open(sys.argv[1], 'r') as f:
        config = json.loads(f.read())

    remote_sync(config)


def remote_sync(config):
    """
    Push newly fetched data to remote repository
    """

    #import pdb; pdb.set_trace()   # debugging mode

    root = config['local']['root_dir']

    # run standard git workflow to push updates
    os.system('git -C %s pull origin master'%(root))
    os.system('git -C %s add .'%(root))
    os.system('git -C %s commit -m "Update at `date`"'%(root))
    os.system('git -C %s push origin master'%(root))




if __name__ == "__main__":
    main()
