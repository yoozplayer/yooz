#!/usr/bin/python3

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

from PyQt5.QtWidgets import QMainWindow, QFrame, QRadioButton, QAction, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QComboBox, QLabel, QSpinBox
from PyQt5.QtGui import QIcon





class MainWindow_Ui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Yooz')    
        self.setWindowIcon(QIcon.fromTheme('mpv'))
 

        # toolbar
        self.toolbar = self.addToolBar('mpv')

        # play video action
        self.playAction = QAction(QIcon.fromTheme('media-playback-start'), 'Play', self, statusTip = 'Play', triggered = self.playVideo, shortcut = 'Ctrl+P')

        # stop action
        self.stopAction = QAction(QIcon.fromTheme('media-playback-stop'), 'Stop', self, statusTip = 'Stop', triggered = self.stopVideo, shortcut = 'Ctrl+S')       

        # exit
        self.exitAction = QAction(QIcon.fromTheme('exit'), 'Exit', self, statusTip = 'Exit', shortcut = 'Ctrl+Q', triggered = self.closeEvent)

        # help
        self.aboutAction = QAction(QIcon.fromTheme('about'), 'About', self, statusTip = 'About', shortcut = 'Ctrl+A', triggered = self.showAboutWindow)

        self.toolbar.addAction(self.playAction)
        self.toolbar.addAction(self.stopAction)
        self.toolbar.addAction(self.exitAction)

        # menu
        menubar = self.menuBar()
        file_menu = menubar.addMenu('&File')
        file_menu.addAction(self.playAction)
        file_menu.addAction(self.stopAction)
        file_menu.addAction(self.exitAction)
        
        help_menu = menubar.addMenu('&Help')
        help_menu.addAction(self.aboutAction)
        
        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)

        VBox = QVBoxLayout(self.centralwidget) 

        # link
        link_HBox = QHBoxLayout()

        self.link_lineEdit = QLineEdit(self.centralwidget)

        # resolution_comboBox
        self.resolution_comboBox = QComboBox(self.centralwidget)

        resolution_list = ['144', '240', '360', '480', '720', '1080', 'Best']
        self.resolution_comboBox.addItems(resolution_list)


        link_HBox.addWidget(self.resolution_comboBox)
        link_HBox.addWidget(self.link_lineEdit)

        VBox.addLayout(link_HBox)

        # radio buttons
        radio_VBox = QVBoxLayout()

        self.radioButton0 = QRadioButton("No Proxy")
        radio_VBox.addWidget(self.radioButton0)
		
        self.radioButton1 = QRadioButton("Torify")
        radio_VBox.addWidget(self.radioButton1)

        self.radioButton2 = QRadioButton("Proxy")
        radio_VBox.addWidget(self.radioButton2)

        VBox.addLayout(radio_VBox)

        # proxy settings
        self.proxy_frame = QFrame(self.centralwidget)
        self.proxy_frame.setFrameShape(QFrame.StyledPanel)
        self.proxy_frame.setFrameShadow(QFrame.Raised)

        proxy_Vbox = QVBoxLayout(self.proxy_frame)

        # http proxy
        http_HBox = QHBoxLayout()

        self.http_ip_label = QLabel(self.proxy_frame)
        self.http_ip_label.setText('http/https proxy: ')
        self.http_ip_lineEdit = QLineEdit(self.proxy_frame)

        self.http_port_label = QLabel(self.proxy_frame)
        self.http_port_label.setText('Port:')
        self.http_port_spinBox = QSpinBox(self.proxy_frame)
        self.http_port_spinBox.setMaximum(65535)
        self.http_port_spinBox.setSingleStep(1)

        for item in self.http_ip_label, self.http_ip_lineEdit, self.http_port_label, self.http_port_spinBox:
            http_HBox.addWidget(item)
        
        proxy_Vbox.addLayout(http_HBox)


        # socks proxy
        socks_HBox = QHBoxLayout()

        self.socks_ip_label = QLabel(self.proxy_frame)
        self.socks_ip_label.setText('socks proxy: ')
        self.socks_ip_lineEdit = QLineEdit(self.proxy_frame)

        self.socks_port_label = QLabel(self.proxy_frame)
        self.socks_port_label.setText('Port:')
        self.socks_port_spinBox = QSpinBox(self.proxy_frame)
        self.socks_port_spinBox.setMaximum(65535)
        self.socks_port_spinBox.setSingleStep(1)

        for item in self.socks_ip_label, self.socks_ip_lineEdit, self.socks_port_label, self.socks_port_spinBox:
            socks_HBox.addWidget(item)
        
        proxy_Vbox.addLayout(socks_HBox)


        VBox.addWidget(self.proxy_frame)

