#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import platform
import sys

if platform.system() == 'Windows':
    BASE_DIR = '\\'.join(os.path.abspath(os.path.dirname(__file__)).split('\\')[:-1])
else:
    BASE_DIR = '/'.join(os.path.abspath(os.path.dirname(__file__)).split('/')[:-1])
sys.path.append(BASE_DIR)

from src.scripts import client

if __name__ == '__main__':
    client()

