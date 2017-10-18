# -*- coding: utf-8 -*-

"""
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import os
import platform
from yooz.scripts import osCommands
from yooz.scripts import browser_integration


# Checking dependencies!
# PyQt5
try:
    import PyQt5
    print('python3-pyqt5 is found')
except:
    print('Error : python3-pyqt5 is not installed!')

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
else:
    print('MPV is found!')

# youtube-dl
answer = os.system('youtube-dl --version 1>/dev/null')
if answer != 0:
    print("youtube-dl is not installed!")
else:
    print('youtube-dl is found!')


# paplay
answer = os.system('paplay --version 1>/dev/null')
if answer != 0:
    print("Warning: paplay not installed!You need pulseaudio for sound notifications!")
else:
    print('paplay is found!')

# initialization
home_address = os.path.expanduser("~")

# os_type >> Linux or Darwin(Mac osx) or Windows(Microsoft Windows) or
# FreeBSD or OpenBSD
os_type = platform.system()

if os_type == 'Linux' or os_type == 'FreeBSD' or os_type == 'OpenBSD':
# config folder .
    config_folder = os.path.join(
        str(home_address), ".config/yooz")
elif os_type == 'Darwin':
    config_folder = os.path.join(
        str(home_address), "Library/Application Support/yooz")
elif os_type == 'Windows':
    config_folder = os.path.join(
        str(home_address), 'AppData', 'Local', 'yooz')


# create config folder
osCommands.makeDirs(config_folder)

# history_file contains history of played links.
history_file = os.path.join(config_folder, 'history')

# create a file for saving links in history
if not(os.path.isfile(history_file)):
    f = open(history_file, 'w')
    f.close()
else:
    # finding number of lines in log_file
    with open(history_file) as f:
        lines = sum(1 for _ in f)

    # if number of lines in log_file is more than 10, then clean older links
    if lines > 10:
        f = open(history_file, 'r')
        f_lines = f.readlines()
        f.close()

        line_counter = 1
        f = open(history_file, 'w')
        f_lines = f_lines.reverse()
        for line in f_lines:
            if line_counter < 11:
                f.writelines(str(line))
            else:
                break

            line_counter = line_counter + 1

        f.close()

# Browser integration for Firefox and chromium and google chrome
for browser in ['chrome', 'chromium', 'opera', 'vivaldi', 'firefox']:
   browser_integration.browserIntegration(browser)


