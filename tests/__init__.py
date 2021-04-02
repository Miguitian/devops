#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    desc: init文件,用于定位PROJECT_ROOT
    author: miguitian
    date: 2021-03-31
"""
import os
_project_root = os.path.dirname(
    os.path.dirname(
        os.path.realpath(__file__)
    )
)

print(_project_root)