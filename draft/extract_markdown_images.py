# -*- coding: utf-8 -*-
# Python3

"""
File: backup-markdown-blog-images.py
Author: Solomon Xie
Email: solomonxiewise@gmail.com
Github: https://github.com/solomonxie
Description: Search all images linked in github issues or comments, download to local folder for backing up
Workflow:
   - [ ] Search all markdown files in a folder (os.walk())
   - [x] Get all image links out of markdown files (Regular Expression)
   - [ ] Prepare local git repo (git pull)
   - [ ] Download all images (wget) to a local git repo
   - [ ] Git add & commit & push to the image repo
   - [ ] Wait for next round check (crontab)

"""

import os
import re


def main():
    filename = './dataset/img_url_matching.md'
    search_dir = './dataset/'
    local_dump = '/Volumes/SD/Workspace/repos/user_content_media/issues-images/solomonxie.github.io/'
    tmpfile = '/tmp/urls.txt'

    #import pdb;pdb.set_trace()
    for root, subdir, filenames in os.walk(search_dir):
        print(root, subdir)
        for fn in filenames:
            print(fn)
            #if '.md' in filename:
            urls = match_img_urls(root+fn)
            print(len(urls))

    return
    # export urls to a .txt file for downloading
    with open(tmpfile, 'w') as f:
        f.write('\n'.join(urls))

    # Download all images from the url list
    os.system('wget --random-wait -nc --limit-rate 300k -i %s -P %s'%(tmpfile, folder))


def match_img_urls(filename):
    """
    :desc: Docstring for match_img_urls.
    :returns: [] list. a list of url strings
    :matching: ![image](https://user-images.githubusercontent.com/14041622/40187586-70e7343c-5a2a-11e8-83ab-e36804921b73.png)
    :cmd: $ wget --random-wait -nc --limit-rate 300k -i List.txt ./folder/
    :workflow: Could be replaced by "awk" command to perform a faster matching
    """
    if os.path.exists(filename) is False:
        return []

    with open(filename, 'r') as f:
        content = f.read()

    # RegExp for matching image urls
    pattern = re.compile(r'\!\[.+\]\((.+)\)')
    urls = pattern.findall(content)

    return urls


if __name__ == "__main__":
    main()
