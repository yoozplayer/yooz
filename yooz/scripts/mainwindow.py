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

import sys
import os
from PyQt5.QtWidgets import QApplication
from yooz.gui.mainwindow_ui import MainWindow_Ui
from yooz.scripts.about import AboutWindow
from functools import partial
from PyQt5.QtCore import QSize, QPoint, QThread, pyqtSignal
import platform

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
history_file = os.path.join(config_folder, 'history')

global radio_button_number
radio_button_number = 0


class Play(QThread):
    EXITSTATUS = pyqtSignal(int)

    def __init__(self, shell):
        QThread.__init__(self)
        self.shell = shell

    def run(self):
        # run bash script in /tmp
        exit_status = int(os.system(self.shell + ' /tmp/yooz'))
        self.EXITSTATUS.emit(exit_status)

class MainWindow(MainWindow_Ui):
    def __init__(self, yooz_setting, dict):
        super().__init__()
        
        # console arguments and 
        # browser plugin arguments
        # will passed to main window
        # with dict!
        self.dict = dict

        # settings
        self.yooz_setting = yooz_setting
        self.yooz_setting.beginGroup('mainwindow')

        # toggle action for radio buttons
        self.radioButton0.toggled.connect(partial(
            self.radioButtonIsToggled, button=self.radioButton0, number=0))
        self.radioButton1.toggled.connect(partial(
            self.radioButtonIsToggled, button=self.radioButton1, number=1))
        self.radioButton2.toggled.connect(partial(
            self.radioButtonIsToggled, button=self.radioButton2, number=2))

        # deactive stopAction
        self.stopAction.setEnabled(False)

       
        # link
        # check clipboard, if user didn't called yooz with 
        # command line arguments, or browser's plugin,
        # and set link_lineEdit value.
        if not('link' in self.dict.keys()):
            # check clipboard
            clipboard = QApplication.clipboard()
            text = clipboard.text()
            if (("tp:/" in text[2:6]) or ("tps:/" in text[2:7])):
                self.link_lineEdit.setText(str(text))
        else:
            # we have link in dict!
            self.link_lineEdit.setText(dict['link'])




        
        # proxy
        # check dict for proxy value
        if 'proxy' in self.dict.keys():
            global radio_button_number

            # check 'proxy' radio button
            self.radioButton2.setChecked(True)
            radio_button_number = 2

            # active proxy_frame
            self.proxy_frame.setEnabled(True)
 
            # extract proxy information
            # the proxy format must be in this format:
            # socks5://127.0.0.1:1080/
            proxy_dict = dict['proxy']
            proxy_split = proxy.split(':')

            # find ip
            ip_split = proxy_split[1]
            ip_split = ip_split.split('//')
            ip = ip_split[1]

            # find port
            port_split = proxy_split[2] 
            port_split = port_split.split('/')
            port = port_split[0]

            if 'http' in proxy_split[0]:# http/https proxy
                http_ip_lineEdit.setText(str(ip)) 
                http_port_spinBox.setValue(int(port))

            elif 'socks' in proxy_split[0]:# socks proxy
                socks_ip_lineEdit.setText(str(ip)) 
                socks_port_spinBox.setValue(int(port))
 
        else:
            # check yooz_setting for initialization value
            init_proxy = int(self.yooz_setting.value('proxy', 0))
            radio_button_number = init_proxy

            if init_proxy == 0:
                # set 'no proxy' checked in radio buttons
                self.radioButton0.setChecked(True)

                # deactive proxy_frame
                self.proxy_frame.setEnabled(False)

            elif init_proxy == 1:
                # set 'torify' checked in radio buttons
                self.radioButton1.setChecked(True)

                # deactive proxy_frame
                self.proxy_frame.setEnabled(False)

            elif init_proxy == 2:
                # set 'proxy' checked in radio buttons
                self.radioButton2.setChecked(True)

                # active proxy_frame
                self.proxy_frame.setEnabled(True)


            # set http_ip and http_port and socks_ip 
            # and socks_port by yooz_setting's values
            http_ip = self.yooz_setting.value('http_ip', None)
            http_port = self.yooz_setting.value('http_port', None)

            socks_ip = self.yooz_setting.value('socks_ip', None)
            socks_port = self.yooz_setting.value('socks_port', None)

            if http_ip:
                self.http_ip_lineEdit.setText(str(http_ip))

            if http_port:
                self.http_port_spinBox.setValue(int(http_port))

            if socks_port:
                self.socks_ip_lineEdit.setText(str(socks_ip))

            if socks_port:
                self.socks_port_spinBox.setValue(int(socks_port))





        # resolution
        if 'resolution' in self.dict.keys():
            # read resolution value from dict
            init_resolution = self.dict['resolution']
        else:
            # read resolution value from yooz_setting
            init_resolution = self.yooz_setting.value('resolution', None)



        # resolution_index is the number of video height in resolution_comboBox
        try:
            resolution_number = int(init_resolution) 
            if resolution_number <= 144:
                resolution_index = 0
            elif resolution_number <= 240:
                resolution_index = 1
            elif resolution_number <= 360:
                resolution_index = 2
            elif resolution_number <= 480:
                resolution_index = 3
            elif resolution_number <= 720:
                resolution_index = 4
            elif resolution_number <= 1080:
                resolution_index = 5
        except:
            # set resolution for Best quality
            resolution_index = 6

        # set index in resolution_comboBox
        self.resolution_comboBox.setCurrentIndex(resolution_index)

        # a list for running AboutWindow
        self.about_window_list = []


# set window size and position
        size = self.yooz_setting.value(
            'size', QSize(500, 300))
        position = self.yooz_setting.value(
            'position', QPoint(300, 300))
        self.resize(size)
        self.move(position)


        self.yooz_setting.endGroup()
        # show window
        self.show()

    
    def playVideo(self, button):
        # deactive playAction and active stopAction
        self.playAction.setEnabled(False)
        self.stopAction.setEnabled(True)
        self.centralwidget.setEnabled(False)

        # get link and resolution
        link = self.link_lineEdit.text()
        video_resolution = self.resolution_comboBox.currentText()
        
        # add link to the history_file
        f = open(history_file, 'a')
        f.writelines(link + '\n')
        f.close()

        # create a file in /tmp.
        # a file will created in /tmp with name of yooz
        # yooz contains some bash commands,
        # like proxy commands and mpv commands.
        f = open('/tmp/yooz', 'w')

        # finding shell path 
        if os_type == 'Linux' or os_type == 'OpenBSD' or os_type == 'FreeBSD':
            # finding shell
            shell_list = ['/bin/bash', '/usr/local/bin/bash', '/bin/sh', '/usr/local/bin/sh', '/bin/ksh', '/bin/tcsh']
    
            for shell in shell_list:
                if os.path.isfile(shell):
                    # defining shebang
                    shebang = '#!' + shell
                    break



        f.writelines(shebang + '\n') 

        # mpv command
        if video_resolution != 'Best':
            mpv_command = 'mpv --ytdl-format "best[height<={}]" "{}"'.format(video_resolution, link)
        else:
            mpv_command = 'mpv "{}"'.format(link)


        # proxy_setting
        if radio_button_number == 1:
            mpv_command = 'torify ' + mpv_command
        elif radio_button_number == 2:
            # get ip and port value
            # http and https
            http_ip = self.http_ip_lineEdit.text() 
            http_port = self.http_port_spinBox.value()

            # socks
            socks_ip = self.socks_ip_lineEdit.text() 
            socks_port = self.socks_port_spinBox.value()

            if http_ip != '':
                proxy = '"{}:{}\\"'.format(http_ip, http_port)
                
            elif socks_ip != '':
                proxy = '"socks5://{}:{}\\"'.format(socks_ip, socks_port)
            
            mpv_command = mpv_command + ' --ytdl-raw-options=proxy=\\' + proxy
 
        f.writelines(mpv_command)
        f.close()
        
        # start play_thread
        self.play_thread = Play(shell)    
        self.play_thread.start()
        self.play_thread.EXITSTATUS.connect(self.exitStatusHandler)

    def stopVideo(self):
        # active playAction and deactive stopAction
        self.playAction.setEnabled(True)
        self.stopAction.setEnabled(False)
        self.centralwidget.setEnabled(True)

        # terminate play_thread
        self.play_thread.terminate()

    def exitStatusHandler(self, status):
        # active playAction and deactive stopAction
        self.playAction.setEnabled(True)
        self.stopAction.setEnabled(False)
        self.centralwidget.setEnabled(True)

        print(status)
        if status != 0:
            # show "Failed" message in statusBar
            self.statusBar().showMessage('Failed!')

            # Play notification sound
            os.system('paplay /usr/share/sounds/freedesktop/stereo/dialog-error.oga')
                
    # this method is called when one of proxy radio buttons are toggled
    def radioButtonIsToggled(self,bela ,button, number):
        global radio_button_number
        if button.isChecked():
            radio_button_number = number
            if number == 2:
                # active proxy_frame
                self.proxy_frame.setEnabled(True)
            else:
                # deactive proxy_frame
                self.proxy_frame.setEnabled(False)

    # show about window
    def showAboutWindow(self,button):
        about_window = AboutWindow()
        self.about_window_list.append(about_window)
        self.about_window_list[len(self.about_window_list) - 1].show()

    # exit yooz
    def closeEvent(self, button):
        # terminate play tread
        try:
            self.play_thread.terminate()
        except:
            print('No thread is terminated')

        # save values in yooz_setting
        self.yooz_setting.beginGroup('mainwindow')
 
        # size and position
        self.yooz_setting.setValue('size', self.size())
        self.yooz_setting.setValue('position', self.pos())

        # proxy setting
        self.yooz_setting.setValue('proxy', radio_button_number)

        # resolution
        resolution = self.resolution_comboBox.currentText()
        self.yooz_setting.setValue('resolution', str(resolution))

        # http ip and port 
        self.yooz_setting.setValue('http_ip',
                self.http_ip_lineEdit.text())
        self.yooz_setting.setValue('http_port',
                self.http_port_spinBox.value())

        # socks
        self.yooz_setting.setValue('socks_ip',
                self.socks_ip_lineEdit.text())
        self.yooz_setting.setValue('socks_port',
                self.socks_port_spinBox.value())

        self.yooz_setting.endGroup()

        self.yooz_setting.sync()

                
        # exit app
        sys.exit(0)

