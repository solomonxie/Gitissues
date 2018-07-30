# -*- coding: utf-8 -*-
# Python3. Preferred in virtual enviroment.

"""
Author: Solomon Xie
Email: solomonxiewise@gmail.com
Github: https://github.com/solomonxie
Description: 
    Main entry of the project.
"""

from issues import Issues

#import pdb;pdb.set_trace()
issues = Issues('./.local/gitissues-config.json')
issues.fetch() 

def main():




if __name__ == "__main__":
    main()