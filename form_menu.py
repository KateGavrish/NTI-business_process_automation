from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QComboBox, QMainWindow
from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel, QMessageBox, QCheckBox
import sys
from ecxel_example import *
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
import datetime
from PyQt5 import QtCore

from form_session3 import Session3
from form_session4 import Session4, ListW
from sql.data.__all_models import *


class Ui_Menu(object):
    def setupUi(self, Menu):
        Menu.setObjectName("Menu")
        Menu.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Menu)
        self.centralwidget.setObjectName("centralwidget")
        self.req = QtWidgets.QPushButton(self.centralwidget)
        self.req.setGeometry(QtCore.QRect(220, 270, 361, 91))
        self.req.setObjectName("req")
        self.balance = QtWidgets.QPushButton(self.centralwidget)
        self.balance.setGeometry(QtCore.QRect(220, 170, 371, 91))
        self.balance.setObjectName("balance")
        Menu.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Menu)
        self.statusbar.setObjectName("statusbar")
        Menu.setStatusBar(self.statusbar)

        self.retranslateUi(Menu)
        QtCore.QMetaObject.connectSlotsByName(Menu)

    def retranslateUi(self, Menu):
        _translate = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(_translate("Menu", "Меню"))
        self.req.setText(_translate("Menu", "Заявки"))
        self.balance.setText(_translate("Menu", "Остатки"))


class Menu(QMainWindow, Ui_Menu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.req.clicked.connect(self.req_win)
        self.balance.clicked.connect(self.balance_win)

    def req_win(self):
        MainWin.show()

    def balance_win(self):
        MainWin1.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWin1 = Session3()
    MainWin = Session4()
    ListW_ = ListW()
    menu = Menu()
    menu.show()
    sys.exit(app.exec())
