#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
from datetime import date


def main():

    remote_sync()


def remote_sync():
    """
    Push newly fetched data to remote repository
    """

    #import pdb; pdb.set_trace()   # debugging mode
    today        = str(date.today())

    # @@ read config file
    with open('config.json', 'r') as f:
        root = json.loads(f.read())

    # run standard git workflow to push updates
    os.system('git -C %s add .'%(root))
    os.system('git -C %s commit -m "Update issues on %s"'%(root,today))
    os.system('git -C %s pull origin master'%(root))
    os.system('git -C %s push origin master'%(root))




if __name__ == "__main__":
    main()
