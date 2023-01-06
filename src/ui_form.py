# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

from downloaderwidget import DownloaderWidget
from episodeswidget import EpisodesWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(30, 10, 401, 121))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.updateTableButton = QPushButton(self.gridLayoutWidget)
        self.updateTableButton.setObjectName(u"updateTableButton")

        self.gridLayout.addWidget(self.updateTableButton, 4, 0, 1, 1)

        self.openXMLButton = QPushButton(self.gridLayoutWidget)
        self.openXMLButton.setObjectName(u"openXMLButton")

        self.gridLayout.addWidget(self.openXMLButton, 1, 0, 1, 1)

        self.pushButton = QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(560, 20, 181, 16))
        self.downloader = DownloaderWidget(self.centralwidget)
        self.downloader.setObjectName(u"downloader")
        self.downloader.setGeometry(QRect(30, 140, 411, 311))
        self.downloader.setAutoFillBackground(True)
        self.episodes = EpisodesWidget(self.centralwidget)
        self.episodes.setObjectName(u"episodes")
        self.episodes.setGeometry(QRect(480, 60, 281, 361))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.createNewWindow)
        self.openXMLButton.clicked.connect(self.downloader.onSendFilepathSignal)
        self.downloader.sendSelectedFilePathSignal.connect(self.episodes.refreshEpisodesFromXML)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.updateTableButton.setText(QCoreApplication.translate("MainWindow", u"todo", None))
        self.openXMLButton.setText(QCoreApplication.translate("MainWindow", u"Open the xml file", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Create New Window", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Podcast player", None))
    # retranslateUi

