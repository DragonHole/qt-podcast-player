from PySide6.QtWidgets import (
    QWidget,
    QListView,
    QVBoxLayout,
    QMessageBox
)

from PySide6.QtGui import (QCursor, QDesktopServices, QGuiApplication, QIcon,
                           QKeySequence, QShortcut, QStandardItem,
                           QStandardItemModel)
from PySide6.QtCore import Slot, QXmlStreamReader, QIODevice, QFile

import xml.etree.ElementTree as ET

DIR_OPEN_ICON = ":/qt-project.org/styles/commonstyle/images/diropen-128.png"

COMPUTER_ICON = ":/qt-project.org/styles/commonstyle/images/computer-32.png"

def class_name(o):
    return o.metaObject().className()

def init_widget(w, name):
    """Init a widget for the gallery, give it a tooltip showing the
       class name"""
    w.setObjectName(name)
    w.setToolTip(class_name(w))

def embed_into_vbox_layout(w, margin=5):
    """Embed a widget into a layout to give it a frame"""
    result = QWidget()
    layout = QVBoxLayout(result)
    layout.setContentsMargins(margin, margin, margin, margin)
    layout.addWidget(w)
    return result

class EpisodesWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.xml_file = None

        self.list_model = QStandardItemModel(0, 1, self)

        # self.list_model.appendRow(QStandardItem(QIcon(DIR_OPEN_ICON), "Directory"))
        # self.list_model.appendRow(QStandardItem(QIcon(COMPUTER_ICON), "Computer"))

        self.list_view = QListView()
        init_widget(self.list_view, "listView")
        self.list_view.setModel(self.list_model)

        vlayout = QVBoxLayout(self)
        vlayout.addWidget(self.list_view)
    
    @Slot(int)
    def on_sld_valueChanged(self, value):
        self.lcd.display(value)
        self.printLabel(value)
        self.logLabel(value)
    
    @Slot(str)
    def refreshEpisodesFromXML(self, filePath):
        # xml_file_read = QFile(filePath)

        # if xml_file_read.open(QIODevice.ReadOnly | QIODevice.Text):
        #     xml = QXmlStreamReader(xml_file_read)
            
        #     while not xml.atEnd():
        #         token = xml.readNext()
        #         #print(token)
        #         if xml.name() == "title" and token == QXmlStreamReader.Characters and QXmlStreamReader.isWhitespace(xml) == False:
        #             print(xml.text())
        #             #self.list_model.appendRow(QStandardItem(QIcon(COMPUTER_ICON), xml.text()))

        #         if xml.hasError():
        #             print('error xml')

            # --------------
            # if xml.readNextStartElement():
            #     if xml.name() == 'rss':
            #         xml.raiseError("Not a podcast RSS file")
            #     while xml.readNextStartElement():
            #         if xml.name() == 'title':
            #             print(xml.readElementText())
            #         else:
            #             xml.skipCurrentElement()

        # else:
        #     QMessageBox.warning(self, "", "Can't Open file " + filePath)

        # xml_file_read.close()

        self.list_model.clear()

        tree = ET.parse(filePath)
        root = tree.getroot()
        if root.tag != 'rss':
            QMessageBox.warning(self, "", "Not rss XML " + filePath)
        
        for child in root[0]:
            print(child.tag, child.attrib)
            if child.tag == 'item':
                episode_title = child.find("title").text
                episode_mp3_url = child.find("enclosure").attrib['url']
                print(episode_title)
                print(episode_mp3_url)
                self.list_model.appendRow(QStandardItem(QIcon(COMPUTER_ICON), episode_title))
