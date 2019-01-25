#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Solomon Xie
Email: solomonxiewise@gmail.com
Github: https://github.com/solomonxie
Description:
"""


def request_url(self, url):
    try:
        r = requests.get(url, timeout=5)

    except Exception as e:
        self.log.error(e)
        self.log.error('Mission aborted.\nAn error occured when requesting:\n%s\n'%url)
        return None

    if r.status_code is not 200:
        self.log.error('Failed on fetching %s due to unexpected response'%url)
        return None

    __limit = r.headers['X-RateLimit-Remaining']
    self.log.debug('Remain %s requests limit in this hour.'%__limit)
    return r

def __define_logger(self, logger_name):
    """
    Should only be applied in main() function of module.
    For sub modules, could simply use logging.getLogger('...') to get a sub-logger after it's declared in main() function
    """
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('\n%(asctime)s - %(name)s - %(levelname)s :\n\n\t%(message)s')

    # make log file path
    if os.path.exists(self.log_dir) is False:
        os.makedirs(self.log_dir)
    last_log = '%s/last.log'%self.log_dir
    daily_log = '{}/{}-{}.log'.format(self.log_dir, logger_name, date.today())

    # create a file handler for logging
    main = logging.FileHandler(last_log, mode='w')
    main.setFormatter(formatter)
    daily = logging.FileHandler(daily_log)
    daily.setFormatter(formatter)

    # create a stream(stdout) handler for logging
    screen  = logging.StreamHandler(stream=None)
    screen.setFormatter(formatter)

    # add handlers to logger object
    logger.addHandler(main)
    logger.addHandler(daily)
    logger.addHandler(screen)

    return logger

def upload_to_github(url):
    """
    Upload image (local/remote) to github repo
    return the file's github raw link
    """
    pass
