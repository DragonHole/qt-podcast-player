# This Python file uses the following encoding: utf-8
import sys
import random

from PySide6.QtCore import Slot, QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o src/ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.windows = []
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(QSize(800, 600))
    
    @Slot()
    def createNewWindow(self):
        window = AnotherWindow()
        self.windows.append(window)
        window.show()
        self.hideUI()

    @Slot()
    def hideUI(self):
        if self.ui.downloader.isVisible():
            self.ui.downloader.setVisible(False) # downloader is the object name
        else:
            self.ui.downloader.setVisible(True) # downloader is the object name


class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent,
    it will appear as a free-floating window.
    """
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window % d" % random.randint(0, 100))
        layout.addWidget(self.label)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
