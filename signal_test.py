import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(188, 267)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(50, 140, 75, 24))
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(30, 40, 104, 71))
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))

        
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    @Slot(str)
    def update_text(self, value):
        self.ui.textEdit.setText(self.ui.textEdit.toPlainText() + value)
        self.ui.textEdit.verticalScrollBar().setValue(
            self.ui.textEdit.verticalScrollBar().maximum()
        )


class Account(QThread):
    textUpdate = Signal(str)

    def run(self):
        print("thread is work")
        print(QThread.currentThread())
        self.textUpdate.emit("Connect to device\n")


if __name__ == "__main__":
    app = QApplication()

    main = MainWindow()
    acc_instance = Account()

    acc_instance.textUpdate.connect(main.update_text)
    main.ui.pushButton.clicked.connect(acc_instance.start)

    main.show()

    sys.exit(app.exec_())