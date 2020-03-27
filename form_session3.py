from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QComboBox, QMainWindow
from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel, QMessageBox
import sys
from ecxel_example import *
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
import datetime
from PyQt5 import QtCore
from sql.data.__all_models import *
from make_xlsx_session_3 import *


class Ui_Session3(object):
    def setupUi(self, Session3):
        Session3.setObjectName("Session3")
        Session3.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Session3)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 0, 351, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 25, 300, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        b = datetime.date.today().year
        b1 = datetime.date.today().month
        b2 = datetime.date.today().day

        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(328, 37, 161, 28))
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
        self.close_ = QtWidgets.QPushButton(self.centralwidget)
        self.close_.setGeometry(QtCore.QRect(190, 510, 141, 51))
        self.close_.setObjectName("close")
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
        self.close_.setText(_translate("Session3", "Закрыть"))
        self.print_d.setText(_translate("Session3", "Печать"))


class Session3(QMainWindow, Ui_Session3):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.size_table = 0

        self.run.clicked.connect(self.info_output)
        self.close_.clicked.connect(self.close_win)
        self.print_d.clicked.connect(self.print_document)

        self.info_output()

    def balance_calculation(self):
        """Подсчет остатков"""
        date = datetime.date(*self.dateEdit.date().getDate())
        complect_with_balance = dict()
        db_session.global_init('sql/db/drons1.sqlite')

        session = db_session.create_session()
        for user in session.query(count_for_dron.QuanForDron):
            if user.name_det not in complect_with_balance:
                complect_with_balance[user.name_det] = int(user.quantity)
            else:
                complect_with_balance[user.name_det] += int(user.quantity)
        for user in session.query(balance.Balance).filter(balance.Balance.date <= date):
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
        self.size_table = len(complect_with_balance)
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
        self.close()

    def read_table(self):
        """ эта функция возвращает данные таблицы
            список состоит из списков,  вот так:
            [["комплектющее", "серийный номер", "количество"]]"""

        info_table = []
        for i in range(self.size_table):
            a = []
            for j in range(3):
                a.append(self.tableWidget.item(i, j).text())
            info_table.append(a)
        return info_table

    def print_document(self):
        """Печать документа"""
        list_of_balances = self.read_table()
        path_to_file = QFileDialog.getSaveFileName(self, 'Open file', None, "(*.xlsx)")[0]
        if path_to_file:
            make_xlsx_table(path_to_file, list_of_balances)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWin = Session3()
    MainWin.show()
    sys.exit(app.exec())
