#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Solomon Xie
Email: solomonxiewise@gmail.com
Github: https://github.com/solomonxie
Description:
    Contains all the API calls, urls, parameters and such methods
"""

import requests

class API:
    """
        Be the Root parent class for all the children class like repo, issue, comment
    """
    def __init__(self):
        pass

    def request_api(self, url):
        r = self.__request(url)
        print('Remain {} requests limit in this hour.'.format(self.get_remain_limits(r)))
        pass

    def get_remain_limits(self, resp):
        return resp.headers['X-RateLimit-Remaining']

    def get_header_paginations(self, resp):
        links = resp.headers['Link']
        """
        <https://api.github.com/repositories/41742246/issues/49/comments?client_id=0c...ed&client_secret=da..5b&q=addClass&page=2>; rel="next",
        <https://api.github.com/repositories/41742246/issues/49/comments?client_id=0c...ed&client_secret=da..5b&q=addClass&page=4>; rel="last"
        """
        pass


    def __request(self, url):
        try:
            r = requests.get(url, timeout=5)
            if r.status_code is not 200:
                print('Failed on fetching {} due to unexpected response'.format(url))
                r = None
        except Exception:
            print('Mission aborted.\nAn error occured when requesting:\n{}\n'.format(url))
            r = None
        return r

    def get_api_repo(self):
        pass

    def get_api_issue(self):
        pass

    def get_api_comments(self):
        pass
