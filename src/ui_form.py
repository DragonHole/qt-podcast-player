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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

from downloaderwidget import DownloaderWidget
from episodeswidget import EpisodesWidget
from mediaplayerwidget import MediaPlayerWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(805, 600)
        self.actionQAction1 = QAction(MainWindow)
        self.actionQAction1.setObjectName(u"actionQAction1")
        self.actionQAction2 = QAction(MainWindow)
        self.actionQAction2.setObjectName(u"actionQAction2")
        self.actionQAction3 = QAction(MainWindow)
        self.actionQAction3.setObjectName(u"actionQAction3")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.downloader = DownloaderWidget(self.centralwidget)
        self.downloader.setObjectName(u"downloader")
        self.downloader.setGeometry(QRect(170, 70, 261, 481))
        self.downloader.setAutoFillBackground(True)
        self.episodes = EpisodesWidget(self.centralwidget)
        self.episodes.setObjectName(u"episodes")
        self.episodes.setGeometry(QRect(440, 70, 351, 481))
        self.mediaplayer = MediaPlayerWidget(self.centralwidget)
        self.mediaplayer.setObjectName(u"mediaplayer")
        self.mediaplayer.setGeometry(QRect(160, 0, 641, 61))
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 0, 161, 551))
        self.verticalLayoutWidget = QWidget(self.groupBox)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 20, 166, 531))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Arial Rounded MT Bold"])
        font.setPointSize(19)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.openXMLButton = QPushButton(self.verticalLayoutWidget)
        self.openXMLButton.setObjectName(u"openXMLButton")

        self.verticalLayout.addWidget(self.openXMLButton)

        self.updateTableButton = QPushButton(self.verticalLayoutWidget)
        self.updateTableButton.setObjectName(u"updateTableButton")

        self.verticalLayout.addWidget(self.updateTableButton)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 805, 24))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menuMenu.addAction(self.actionQAction1)
        self.menuMenu.addAction(self.actionQAction2)
        self.menuMenu.addAction(self.actionQAction3)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.createNewWindow)
        self.openXMLButton.clicked.connect(self.downloader.onSendFilepathSignal)
        self.downloader.sendSelectedFilePathSignal.connect(self.episodes.refreshEpisodesFromXML)
        self.episodes.sendSelectedMediaUrlSignal.connect(self.mediaplayer.setPlayingMedia)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionQAction1.setText(QCoreApplication.translate("MainWindow", u"QAction1", None))
        self.actionQAction2.setText(QCoreApplication.translate("MainWindow", u"QAction2", None))
        self.actionQAction3.setText(QCoreApplication.translate("MainWindow", u"QAction3", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Podcasts", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Podcast player", None))
        self.openXMLButton.setText(QCoreApplication.translate("MainWindow", u"Open the xml file", None))
        self.updateTableButton.setText(QCoreApplication.translate("MainWindow", u"todo...", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Create New Window", None))
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
    # retranslateUi

