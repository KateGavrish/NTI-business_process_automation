from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QComboBox, QMainWindow
from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel, QMessageBox
import sys
from ecxel_example import *
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
import datetime
from PyQt5 import QtCore
from sql.data.__all_models import *


class Ui_Session3(object):
    def setupUi(self, Session3):
        Session3.setObjectName("Session3")
        Session3.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Session3)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(390, 10, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        b = datetime.date.today().year
        b1 = datetime.date.today().month
        b2 = datetime.date.today().day

        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(610, 20, 161, 41))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDisplayFormat("yyyy-MM-dd")
        self.dateEdit.setDate(QtCore.QDate(b, b1, b2))

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 70, 741, 421))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.run = QtWidgets.QPushButton(self.centralwidget)
        self.run.setGeometry(QtCore.QRect(30, 510, 151, 51))
        self.run.setObjectName("run")
        self.close = QtWidgets.QPushButton(self.centralwidget)
        self.close.setGeometry(QtCore.QRect(180, 510, 141, 51))
        self.close.setObjectName("close")
        self.print_d = QtWidgets.QPushButton(self.centralwidget)
        self.print_d.setGeometry(QtCore.QRect(650, 510, 121, 51))
        self.print_d.setObjectName("print_d")
        Session3.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Session3)
        self.statusbar.setObjectName("statusbar")
        Session3.setStatusBar(self.statusbar)

        self.retranslateUi(Session3)
        QtCore.QMetaObject.connectSlotsByName(Session3)

    def retranslateUi(self, Session3):
        _translate = QtCore.QCoreApplication.translate
        Session3.setWindowTitle(_translate("Session3", "Session3"))
        self.label.setText(_translate("Session3", "Остатки комплектующих"))
        self.label_2.setText(_translate("Session3", "Показывать остатки на:"))
        self.run.setText(_translate("Session3", "Выполнить"))
        self.close.setText(_translate("Session3", "Закрыть"))
        self.print_d.setText(_translate("Session3", "Печать"))


class Session3(QMainWindow, Ui_Session3):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.run.clicked.connect(self.info_output)
        self.close.clicked.connect(self.close_win)
        self.print_d.clicked.connect(self.print_document)

    def balance_calculation(self):
        """Подсчет остатков"""
        date = self.dateEdit.date().currentDate().toPyDate()
        complect_with_balance = dict()
        db_session.global_init('sql/db/drons1.sqlite')

        session = db_session.create_session()
        for user in session.query(count_for_dron.QuanForDron):
            if user.name_det not in complect_with_balance:
                complect_with_balance[user.name_det] = int(user.quantity)
            else:
                complect_with_balance[user.name_det] += int(user.quantity)
        for user in session.query(balance.Balance).filter(balance.Balance.date <= date):
            print(user.date, date)
            if user.name_det not in complect_with_balance:
                complect_with_balance[user.name_det] = int(user.quantity)
            else:
                complect_with_balance[user.name_det] += int(user.quantity)
        return complect_with_balance

    def info_output(self):
        """Вывод информации в таблицу"""
        self.tableWidget.clear()
        complect_with_balance = self.balance_calculation()
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(len(complect_with_balance))
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem('Номер'))
        self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem('Комплектующее'))
        self.tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem('Остаток'))
        i = 1
        for item in complect_with_balance.keys():
            itm = QTableWidgetItem(f'{i}')
            itm.setFlags(QtCore.Qt.ItemIsEnabled)

            itm1 = QTableWidgetItem(item)
            itm1.setFlags(QtCore.Qt.ItemIsEnabled)

            itm2 = QTableWidgetItem(str(complect_with_balance[item]))
            itm2.setFlags(QtCore.Qt.ItemIsEnabled)

            self.tableWidget.setItem(i - 1, 0, itm)
            self.tableWidget.setItem(i - 1, 1, itm1)
            self.tableWidget.setItem(i - 1, 2, itm2)

            i += 1

        self.tableWidget.resizeColumnsToContents()

    def close_win(self):
        """Закрытие программы"""
        MainWindow.close()

    def print_document(self):
        """Печать документа"""
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = Session3()
    MainWindow.show()
    sys.exit(app.exec())
