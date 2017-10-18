#!/usr/bin/env python3
# coding: utf-8

import os
import shutil
import sys

uid = os.getuid()
if uid != 0:
    print('run this script as root.')
    sys.exit(1)


# clearing after installation finished!
for folder in  [ 'build', 'dist', 'root', 'yooz.egg-info']:
    if os.path.isdir(folder):
        shutil.rmtree(folder)
        print(str(folder)
            + ' is removed!')
