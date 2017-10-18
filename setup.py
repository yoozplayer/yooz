#!/usr/bin/env python3
# coding: utf-8


import os.path
import warnings
import sys
import platform
import shutil

# finding os platform
os_type = platform.system()

if os_type == 'Linux' or os_type == 'FreeBSD' or os_type == 'OpenBSD':
    from setuptools import setup, Command, find_packages
    setuptools_available = True
    print(os_type + " detected!")
else:
    print('This script is only work for GNU/Linux or BSD!')
    sys.exit(1)

# Checking dependencies!
# PyQt5
try:
    import PyQt5
    print('python3-pyqt5 is found')
except:
    print('Error : python3-pyqt5 is not installed!')
    sys.exit(1)

# python3-setproctitle
try:
    import setproctitle
    print('python3-setproctitle is found!')
except:
    print("Warning: setproctitle is not installed!")

# mpv
answer = os.system('mpv --version 1>/dev/null')
if answer != 0:
    print("MPV is not installed!")
    sys.exit(1)
else:
    print('MPV is found!')

# youtube-dl
answer = os.system('youtube-dl --version 1>/dev/null')
if answer != 0:
    print("youtube-dl is not installed!")
    sys.exit(1)
else:
    print('youtube-dl is found!')


# paplay
answer = os.system('paplay --version 1>/dev/null')
if answer != 0:
    print("Warning: paplay not installed!You need pulseaudio for sound notifications!")
else:
    print('paplay is found!')

# sound-theme-freedesktop
if os_type == 'Linux':
    notifications_path = '/usr/share/sounds/freedesktop/stereo/'
elif os_type == 'FreeBSD' or os_type == 'OpenBSD':
    notifications_path = '/usr/local/share/sounds/freedesktop/stereo/'

if os.path.isdir(notifications_path):
    print('sound-theme-freedesktop is found!')
else:
    print('Warning: sound-theme-freedesktop is not installed! you need this package for sound notifications!')
 



DESCRIPTION = 'Yooz'
LONG_DESCRIPTION = """
Yooz is a online video player based on MPV
"""

if os_type == 'Linux':
    DATA_FILES = [
        ('/usr/share/applications/', ['xdg/yooz.desktop'])
        ]
elif os_type == 'FreeBSD' or os_type == 'OpenBSD':
    DATA_FILES = [
        ('/usr/local/share/applications/', ['xdg/yooz.desktop']),
        ]



# finding current directory
cwd = os.path.abspath(__file__)
setup_dir = os.path.dirname(cwd)

#clearing __pycache__
src_pycache = os.path.join(setup_dir, 'yooz', '__pycache__')
gui_pycache = os.path.join(setup_dir, 'yooz', 'gui', '__pycache__')
scripts_pycache = os.path.join(setup_dir, 'yooz', 'scripts', '__pycache__')

for folder in [src_pycache, gui_pycache, scripts_pycache]:
    if os.path.isdir(folder):
        shutil.rmtree(folder)
        print(str(folder)
            + ' is removed!')


setup(
    name = 'yooz',
    version = '1.0',
    license = 'GPL3',
    description = DESCRIPTION,
    long_description = LONG_DESCRIPTION,
    include_package_data=True,
    url = 'https://github.com/alireza_amirsamimi/yooz',
    author = 'AliReza AmirSamimi',
    author_email = 'alireza.amirsamimi@gmail.com',
    maintainer = 'AliReza AmirSamimi',
    maintainer_email = 'alireza.amirsamimi@gmail.com',
    packages = (
        'yooz',
        'yooz.scripts', 'yooz.gui',
        ),
    data_files = DATA_FILES,
    entry_points={
        'console_scripts': [
              'yooz = yooz.__main__'
        ]
    }
)
