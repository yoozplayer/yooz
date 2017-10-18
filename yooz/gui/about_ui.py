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

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QIcon


class AboutWindow_Ui(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("About Yooz Player")
        self.setWindowIcon(QIcon.fromTheme('mpv'))

        self.title_label = QLabel(self)
        self.version_label = QLabel(self)
        self.name_label = QLabel(self)
        self.site_label = QLabel(self)
        self.pushButton = QPushButton(self)

        VBox = QVBoxLayout(self)

        for item in self.title_label, self.version_label, self.name_label, self.site_label, self.pushButton:
            VBox.addWidget(item)

        self.title_label.setText("Yooz Player")
        self.version_label.setText("Version 1.0")

        self.name_label.setText(
            "\nAliReza AmirSamimi\nMohammadreza Abdollahzadeh\nSadegh Alirezaie\nMostafa Asadi\nMohammadAmin Vahedinia\nJafar Akhondali")
        self.site_label.setText(
            "<a href=https://yooz.github.io>https://yooz.github.io</a>")
        self.pushButton.setText("Ok")


