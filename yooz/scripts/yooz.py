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

import yooz.scripts.initialization
import argparse
from yooz.scripts.mainwindow import MainWindow
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QSettings
import os
import platform
try:
    from setproctitle import setproctitle
    setproctitle("Yooz Player")
except:
    print('setproctitle is not installed!')



home_address = os.path.expanduser("~")

# os_type >> Linux or Darwin(Mac osx) or Windows(Microsoft Windows) or
# FreeBSD or OpenBSD
os_type = platform.system()
# creating  terminal arguments  

parser = argparse.ArgumentParser(description='Yooz')
parser.add_argument('browser', nargs = '?', default = 'no', help='this switch is used for browsers native messaging in Linux and Mac')
parser.add_argument('--link', action='store', nargs = 1, help='link.(Use "" for links)')
parser.add_argument('--resolution', action='store', nargs = 1, help='Set resolution for video.')
parser.add_argument('--proxy', action='store', nargs = 1, help='proxy information.proxy format\
        must be in this format:\n\
        socks5://127.0.0.1:1080/\n\
        Only http, https and socks5 proxy is accepted')
parser.add_argument('--play', action='store', nargs = 1, help='yes >> play video immediatly after opening GUI')
parser.add_argument('--parent-window', action='store', nargs = 1, help="this switch is used for browser's plugin native messaging in Windows")
parser.add_argument('--version', action='version', version='Yooz Player 1.0')
args = parser.parse_args()


# console arguments and 
# browser plugin arguments
# will passed to main window
# with dict!
dict = {}
if args.browser != 'no' or args.parent_window:

# Platform specific configuration
    if os_type == "Windows":
  # Set the default I/O mode to O_BINARY in windows
        import msvcrt
        msvcrt.setmode(sys.stdin.fileno(), os.O_BINARY)
        msvcrt.setmode(sys.stdout.fileno(), os.O_BINARY)


    # Send message to browser extension
    message = '{"enable": true, "version": "1.85"}'.encode('utf-8')
    sys.stdout.buffer.write((struct.pack('I', len(message))))
    sys.stdout.buffer.write(message)
    sys.stdout.flush()

    

    text_length_bytes = sys.stdin.buffer.read(4)

    # Unpack message length as 4 byte integer.
    text_length = struct.unpack('i', text_length_bytes)[0]

    # Read the text (JSON object) of the message.
    text = sys.stdin.buffer.read(text_length).decode("utf-8")
    if text:
        if not 'url' in text:
            sys.exit(0)

        data = json.loads(text)
        url = str(data['url'])

        # get link and resolution and proxy information.
        if url:
            args.link = str(url)
            if 'resolution' in data.keys():
                args.resolution = data['resolution']
                
            if 'proxy' in data.keys():
                args.proxy = data['proxy']

            if 'play' in data.keys():
                args.play = data['play']

if args.link:
    dict['link'] = str(args.link)

if args.proxy:
    dict['proxy'] = str(args.proxy)

if args.resolution:
    dict['resolution'] = str(args.resolution)

if args.play:
    dict['play'] = str(args.play)



def main():
    # load yooz_settings
    yooz_setting = QSettings('yooz', 'yooz')

    yooz = QApplication(sys.argv)
        
    # console arguments and 
    # browser plugin arguments
    # will passed to main window
    # with dict!
    mainwindow = MainWindow(yooz_setting, dict)
    sys.exit(yooz.exec_())
