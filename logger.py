#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    desc: 日志相关
    author: miguitian
    date: 2021-02-01
"""

import sys
import traceback

try:
    from __init__ import _project_root

    sys.path.append(_project_root)
except Exception:
    traceback.print_exc()
import os
import logging
import logging.handlers
from colorlog import ColoredFormatter
from config import config_manager

LOG_LEVEL_MAPPINGS = {
    'notset': logging.NOTSET,
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'error': logging.ERROR,
    'critical': logging.CRITICAL
}


def Logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(LOG_LEVEL_MAPPINGS[config_manager.LOG_LEVEL])
    LOGFORMAT = '%(log_color)s%(asctime)s-%(name)s-%(levelname)s:  %(message)s'
    format_str = ColoredFormatter(LOGFORMAT,
                                  log_colors={'DEBUG': 'white', 'INFO': 'bold_white', 'WARNING': 'bold_yellow',
                                              "ERROR": 'bold_red'})

    sh = logging.StreamHandler()
    sh.setFormatter(format_str)

    if config_manager.LOG_PATH:
        if not os.path.exists(config_manager.LOG_PATH):
            os.makedirs(config_manager.LOG_PATH, exist_ok=True)
        th = logging.handlers.RotatingFileHandler(os.path.join(config_manager.LOG_PATH, '{}.log'.format(name)), mode='a',
                                                  maxBytes=1024 * 1024 * 100,
                                                  backupCount=10, encoding='utf-8')
        format_str = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s:  %(message)s')
        th.setFormatter(format_str)
        logger.addHandler(th)

    logger.addHandler(sh)
    return logger


logger = Logger('devops')
