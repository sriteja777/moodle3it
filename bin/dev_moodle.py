#! /usr/bin/env python3

import os
import subprocess

BIN_DIR = os.path.dirname(os.path.realpath(__file__)) + '/'
APP_DIR = os.path.abspath(os.path.join(BIN_DIR, os.pardir)) + '/'

import sys

sys.path.insert(0, APP_DIR)



try:
    print("virtual env")
    env_path = os.environ['MOODLE_VIRTUALENVPATH'] + 'bin/python'
    subprocess.Popen([env_path, APP_DIR + 'all.py'])
except Exception as e:
    pass
    import all
    all.run_engine()
    # subprocess.call(APP_DIR + 'all.py')

