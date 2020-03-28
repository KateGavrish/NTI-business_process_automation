from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QFile
from PyQt5.QtGui import QFont
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QComboBox, QMainWindow
from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel, QMessageBox
import sys
from ecxel_example import *
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
import datetime
from PyQt5 import QtCore
import pyqtgraph as pg
from form_session4 import ListW
from sql.data.__all_models import *
from make_xlsx_session_3 import *


class Ui_Session6(object):
    def setupUi(self, Session6):
        Session6.setObjectName("Session6")
        Session6.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Session6)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 0, 351, 30))
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
        self.dateEdit.setGeometry(QtCore.QRect(273, 37, 161, 28))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDisplayFormat("yyyy-MM-dd")
        self.dateEdit.setDate(QtCore.QDate(b, b1, b2))

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(455, 25, 300, 51))
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_2")

        b = datetime.date.today().year
        b1 = datetime.date.today().month
        b2 = datetime.date.today().day

        self.dateEdit3 = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit3.setGeometry(QtCore.QRect(505, 37, 161, 28))
        self.dateEdit3.setObjectName("dateEdit")
        self.dateEdit3.setCalendarPopup(True)
        self.dateEdit3.setDisplayFormat("yyyy-MM-dd")
        self.dateEdit3.setDate(QtCore.QDate(b, b1, b2))

        self.graphWidget = pg.PlotWidget(self.centralwidget)
        self.graphWidget.setGeometry(QtCore.QRect(10, 100, 750, 450))

        Session6.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Session6)
        self.statusbar.setObjectName("statusbar")
        Session6.setStatusBar(self.statusbar)

        self.retranslateUi(Session6)
        QtCore.QMetaObject.connectSlotsByName(Session6)

    def retranslateUi(self, Session6):
        _translate = QtCore.QCoreApplication.translate
        Session6.setWindowTitle(_translate("Session6", "Session6"))
        self.label.setText(_translate("Session6", "Анализ остатков АКБ"))
        self.label_2.setText(_translate("Session6", "Анализ остатков с:"))
        self.label_3.setText(_translate("Session6", "по"))


class Session6(QMainWindow, Ui_Session6):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.size_table = 0
        self.make_graphic()
        self.dateEdit.dateChanged.connect(self.make_graphic)
        self.dateEdit3.dateChanged.connect(self.make_graphic)

    def make_graphic(self):
        self.graphWidget.clear()
        self.graphWidget.setBackground('w')
        day1 = datetime.date(*list(self.dateEdit.date().getDate())) - datetime.timedelta(days=1)
        day2 = datetime.date(*list(self.dateEdit3.date().getDate())) + datetime.timedelta(days=1)
        #if day2 > datetime.datetime.today():
        #    day2 = datetime.datetime.today()
        #elif day1 > datetime.datetime.today():
        #    print(2)
        #    day2 = datetime.datetime.now()
        #    day2 = day1.date()
        # print(day1)
        db_session.global_init('app/db/drons1.sqlite')
        session = db_session.create_session()
        accums = []
        for good in session.query(details.DetailCategory).filter(details.DetailCategory.category == 'Аккумуляторные батареи'):
            accums.append(good.name_det)
        b = datetime.date.today().year
        b1 = datetime.date.today().month
        b2 = datetime.date.today().day
        if day2 > datetime.date(b, b1, b2):
            day2 = datetime.date(b, b1, b2)
        if day1 > datetime.date(b, b1, b2):
            day1 = datetime.date(b, b1, b2)
        data = dict()
        a = self.balance_calculation(day1)
        a = sum([a[x] for x in a.keys() if x in accums])
        print(a)
        for good in session.query(balance.Balance).filter(balance.Balance.date.between(day1, day2)):
            if good.name_det in accums:
                if good.date in data:
                    data[good.date] += int(good.quantity)
                else:
                    data[good.date] = int(good.quantity)
        ostatki = [a] + [data[x] for x in sorted(data.keys())]
        self.graphWidget.clear()
        days = [f"{day1.year}-{day1.month}-{day1.day}"]
        day = day1
        while day != day2:
            day = day + datetime.timedelta(days=1)
            days.append(f"{day.year}-{day.month}-{day.day}")
        key_data = []
        for i in list(data.keys()):
            key_data.append((f"{i.year}-{i.month}-{i.day}", days.index(f"{i.year}-{i.month}-{i.day}"), data[i]))
        if key_data:
            key_data = sorted(key_data, key=lambda x: x[1])
        ostatki = []
        for i in range(len(key_data)):
            index_start = key_data[i][1]
            index_end = key_data[i + 1][1] if i + 1 < len(key_data) else len(days)
            value = key_data[i][2]
            ostatki += [value] * int(index_end - index_start)
        ostatki = [a] + ostatki
        days = [i for i in range(len(ostatki))]
        if days == [0]:
            days += [0.25]
            ostatki += ostatki
        if ostatki:
            # в переменной days лежат все дни за которые нужна информация об остатках
            # из дб загрузи все данные в переменную ostatki

            # self.graphWidget.addLegend() вдруг понадобится
            self.graphWidget.showGrid(x=True, y=True)
            self.graphWidget.setXRange(0, int(10), padding=0)
            self.graphWidget.setYRange(0, int(max(ostatki) * 1.1), padding=0)

            self.graphWidget.setBackground('w')

            pen = pg.mkPen(color=(0, 255, 0), width=5)
            self.graphWidget.plot(days, ostatki, pen=pen)

    def balance_calculation(self, date):
        """Подсчет остатков"""
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

    def close_win(self):
        """Закрытие программы"""
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ListW_ = ListW()
    MainWin = Session6()
    MainWin.show()
    sys.exit(app.exec())
