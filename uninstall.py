#!/usr/bin/env python3
# coding: utf-8

import platform
import glob
import os
import shutil
import sys

os_type = platform.system()

if os_type == 'Linux':
    path_list = [
    '/usr/share/applications/yooz.desktop',
    '/usr/bin/yooz']

    # find yooz directories in /usr/lib/python3.6/site-packages/
    pattern = os.path.join('/usr/lib/python3.6/site-packages/', 'yooz*')
    for folder in  glob.glob(pattern):
        path_list.append(folder)

    # find yooz directories in /usr/lib/python3.5/site-packages/
    pattern = os.path.join('/usr/lib/python3.5/site-packages/', 'yooz*')
    for folder in  glob.glob(pattern):
        path_list.append(folder)


elif os_type == 'FreeBSD' or os_type == 'OpenBSD':
    path_list = [
    '/usr/local/share/applications/yooz.desktop',
    '/usr/local/bin/yooz']

    # find yooz directories in /usr/lib/python3.6/site-packages/
    pattern = os.path.join('/usr/local/lib/python3.6/site-packages/', 'yooz*')
    for folder in  glob.glob(pattern):
        path_list.append(folder)

    # find yooz directories in /usr/lib/python3.5/site-packages/
    pattern = os.path.join('/usr/local/lib/python3.5/site-packages/', 'yooz*')
    for folder in  glob.glob(pattern):
        path_list.append(folder)


else:
    print('This script is for Linux and BSD')
    sys.exit(1)

uid = os.getuid()
if uid != 0:
    print('run this script as root.')
    sys.exit(1)


for path in path_list:
    if os.path.exists(path):
        if os.path.isfile(path): # if path is for file 
            os.remove(path) # removing file
        else:
            shutil.rmtree(path)  # removing folder
        print(str(path) + ' is removed!')

print('uninstallation is complete!')


