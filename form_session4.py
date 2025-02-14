from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QComboBox, QMainWindow
from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel, QMessageBox, QCheckBox
import sys
from ecxel_example import *
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
import datetime
from PyQt5 import QtCore
from sql.data.__all_models import *
from make_xlsx_session_3 import *


class Ui_ListWin(object):
    def setupUi(self, ListWin):
        ListWin.setObjectName("ListWin")
        ListWin.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(ListWin)
        self.centralwidget.setObjectName("centralwidget")
        self.change = QtWidgets.QPushButton(self.centralwidget)
        self.change.setGeometry(QtCore.QRect(200, 530, 121, 41))
        self.change.setObjectName("change")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 120, 701, 401))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.create = QtWidgets.QPushButton(self.centralwidget)
        self.create.setGeometry(QtCore.QRect(330, 530, 211, 41))
        self.create.setObjectName("create")

        self.select = QtWidgets.QPushButton(self.centralwidget)
        self.select.setGeometry(QtCore.QRect(560, 530, 211, 41))
        self.select.setObjectName("select")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(50, 80, 701, 26))
        self.comboBox.setObjectName("comboBox")
        ListWin.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ListWin)
        self.statusbar.setObjectName("statusbar")
        ListWin.setStatusBar(self.statusbar)

        self.retranslateUi(ListWin)
        QtCore.QMetaObject.connectSlotsByName(ListWin)

    def retranslateUi(self, ListWin):
        _translate = QtCore.QCoreApplication.translate
        ListWin.setWindowTitle(_translate("ListWin", "Список заявок"))
        self.change.setText(_translate("ListWin", "Изменить"))
        self.create.setText(_translate("ListWin", "Создать новую заявку"))
        self.select.setText(_translate("ListWin", "Выбрать"))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(410, 60, 331, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.num_of_request = QtWidgets.QLineEdit(self.centralwidget)
        self.num_of_request.setGeometry(QtCore.QRect(172, 70, 201, 21))
        self.num_of_request.setObjectName("num_of_request")

        b = datetime.date.today().year
        b1 = datetime.date.today().month
        b2 = datetime.date.today().day

        self.date_create = QtWidgets.QDateEdit(self.centralwidget)
        self.date_create.setGeometry(QtCore.QRect(270, 110, 110, 24))
        self.date_create.setCalendarPopup(True)
        self.date_create.setDate(QtCore.QDate(b, b1, b2))
        self.date_create.setObjectName("date_create")
        self.date_otg = QtWidgets.QDateEdit(self.centralwidget)
        self.date_otg.setGeometry(QtCore.QRect(270, 150, 110, 24))
        self.date_otg.setCalendarPopup(True)
        self.date_otg.setObjectName("date_otg")
        self.date_otg.setDate(QtCore.QDate(b, b1, b2))
        self.buyer = QtWidgets.QLineEdit(self.centralwidget)
        self.buyer.setGeometry(QtCore.QRect(160, 180, 221, 21))
        self.buyer.setObjectName("buyer")
        self.state = QtWidgets.QComboBox(self.centralwidget)
        self.state.setGeometry(QtCore.QRect(163, 215, 221, 31))
        self.state.setObjectName("state")
        self.plus_str = QtWidgets.QPushButton(self.centralwidget)
        self.plus_str.setGeometry(QtCore.QRect(520, 250, 100, 41))
        self.plus_str.setObjectName("plus_str")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 70, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(410, 260, 151, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 110, 111, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 150, 201, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 180, 91, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 220, 151, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(410, 30, 211, 21))
        self.label_7.setObjectName("label_7")
        self.create_req = QtWidgets.QPushButton(self.centralwidget)
        self.create_req.setGeometry(QtCore.QRect(110, 310, 591, 61))
        self.create_req.setObjectName("create_req")

        self.list_req = QtWidgets.QPushButton(self.centralwidget)
        self.list_req.setGeometry(QtCore.QRect(110, 370, 591, 61))
        self.list_req.setObjectName("list_req")

        self.fsb_check_box = QtWidgets.QCheckBox('Проверка ФСБ', self.centralwidget)
        self.fsb_check_box.setGeometry(QtCore.QRect(25, 270, 150, 21))

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Session4"))
        self.plus_str.setText(_translate("MainWindow", "+"))
        self.label.setText(_translate("MainWindow", "Номер заявки"))
        self.label_2.setText(_translate("MainWindow", "Добавить поле"))
        self.label_3.setText(_translate("MainWindow", "Дата создания"))
        self.label_4.setText(_translate("MainWindow", "Дата отгрузки/аннулирования"))
        self.label_5.setText(_translate("MainWindow", "Покупатель"))
        self.label_6.setText(_translate("MainWindow", "Состояние заявки"))
        self.label_7.setText(_translate("MainWindow", "Спикок дронов с количеством"))
        self.create_req.setText(_translate("MainWindow", "Создать (изменить, если номер в базе) заявку"))
        self.list_req.setText(_translate("MainWindow", "Список заявок"))


class Session4(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.plus_str.clicked.connect(self.add_string)
        self.create_req.clicked.connect(self.create_request)
        self.list_req.clicked.connect(self.open_list)
        self.ListW_ = ListW()
        self.size_table = 0

        self.init_table()

    def balance_calculation(self):
        """Подсчет остатков"""
        b = datetime.date.today().year
        b1 = datetime.date.today().month
        b2 = datetime.date.today().day

        date = datetime.date(b, b1, b2)
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

    def open_list(self):
        self.ListW_.__init__()
        self.ListW_.show()
        self.close()

    def check(self):
        return self.fsb_check_box.isChecked()

    def init_table(self):
        self.combo_box_options = []
        db_session.global_init('sql/db/drons1.sqlite')
        session = db_session.create_session()
        for user in session.query(drons_cost.DronCost):
            self.combo_box_options.append(user.name_dron)

        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(1)

        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem('Дрон'))
        self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem('Количество'))

        self.add_string()

        combo_box_options = ['Создана', 'Идет сборка', 'Готова к отгрузке',
                             'Запрошено разрешение у ФСБ', 'Аннулирована', 'Отгружена']
        for t in combo_box_options:
            self.state.addItem(t)

    def add_string(self):
        self.tableWidget.setRowCount(self.size_table + 1)
        combo = QComboBox()
        for t in self.combo_box_options:
            combo.addItem(t)
        self.tableWidget.setCellWidget(self.size_table, 0, combo)
        itm1 = QTableWidgetItem('0')
        self.tableWidget.setItem(self.size_table, 1, itm1)

        self.size_table += 1
        self.tableWidget.resizeColumnsToContents()
        self.resize(801, 480)
        self.resize(800, 480)

    def read_table(self):
        """ эта функция возвращает данные таблицы
            список состоит из списков,  вот так:
            [["комплектющее", "количество"]]"""
        info_table = []
        for i in range(self.tableWidget.rowCount()):
            a = []
            for j in range(2):
                if j != 0:
                    a.append(self.tableWidget.item(i, j).text())
                else:
                    a.append(self.tableWidget.cellWidget(i, j).currentText())
            info_table.append(a)
        return info_table

    def parameters(self, num_of_req):
        self.num_of_req = num_of_req

        self.tableWidget.setColumnCount(2)

        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem('Дрон'))
        self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem('Количество'))

        self.add_string()

        combo_box_options = ['Создана', 'Идет сборка', 'Готова к отгрузке',
                             'Запрошено разрешение у ФСБ', 'Аннулирована', 'Отгружена']
        for t in combo_box_options:
            self.state.addItem(t)

        db_session.global_init('sql/db/drons1.sqlite')
        session = db_session.create_session()
        a = []
        score = dict()
        for user in session.query(drons_cost.DronCost):
            score[user.name_dron] = user.cost
        for user in session.query(request_4.DronsToReq).filter(request_4.DronsToReq.num == self.num_of_req):
            a.append([user.dron_name, int(user.quantity) * int(score[user.dron_name])])

        self.tableWidget.setRowCount(len(a))
        for i in range(len(a)):
            for j in range(2):
                item1 = QTableWidgetItem(f'{a[i][1]}')
                self.tableWidget.setItem(i, 1, item1)
                combo = QComboBox()
                combo_box_options = [a[i][0]] + combo_box_options
                for t in combo_box_options:
                    combo.addItem(t)
                self.tableWidget.setCellWidget(i, 0, combo)

        self.tableWidget.resizeColumnsToContents()

        db_session.global_init('sql/db/drons1.sqlite')
        session = db_session.create_session()
        a = []
        for user in session.query(request_4.RequestDron).filter(request_4.RequestDron.number == self.num_of_req).all():
            a.append([user.number, user.date_create, user.date_close, user.buyer, user.state])
            self.buyer.setText(user.buyer)
            self.state.setCurrentText(user.state)
            self.date_create.setDate(user.date_create)
            self.date_otg.setDate(user.date_close)
            self.num_of_request.setText(str(user.number))

    def try_spis(self, num):
        nehv = dict()
        db_session.global_init('sql/db/drons1.sqlite')
        session = db_session.create_session()
        a = []
        ost = self.balance_calculation()
        for user in session.query(request_4.DronsToReq).filter(request_4.DronsToReq.num == num):
            a.append([user.dron_name, int(user.quantity)])
        for x in a:
            for u in session.query(count_for_dron.QuanForDron).filter(count_for_dron.QuanForDron.name_dron == x[0]):
                count_dr = int(x[1])
                if ost[u.name_det] - count_dr * u.quantity < 0:
                    if u.name_det not in nehv:
                        nehv[u.name_det] = abs(ost[u.name_det] - count_dr * u.quantity)
                    else:
                        nehv[u.name_det] += abs(ost[u.name_det] - count_dr * u.quantity)
        return nehv

    def spis(self, num):
        n = self.try_spis(num)
        if n:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Не хватает товара на складе:\n" + '\n'.join([f'{x[0]} {x[1]}' for x in n.items()]))
            okButton = msg.addButton('ОК', QMessageBox.AcceptRole)
            msg.exec()
        else:
            db_session.global_init('sql/db/drons1.sqlite')
            session = db_session.create_session()
            a = []
            ost = self.balance_calculation()
            for user in session.query(request_4.DronsToReq).filter(request_4.DronsToReq.num == num):
                a.append([user.dron_name, int(user.quantity)])
            for x in a:
                for u in session.query(count_for_dron.QuanForDron).filter(count_for_dron.QuanForDron.name_dron == x[0]):
                    count_dr = int(x[1])
                    b1 = datetime.date.today().year
                    b2 = datetime.date.today().month
                    b3 = datetime.date.today().day

                    b = balance.Balance()
                    b.name_det = u.name_det
                    b.quantity = -(ost[u.name_det] - count_dr * u.quantity)
                    b.date = datetime.date(b1, b2, b3)
                    session.add(b)
                    session.commit()

    def create_request(self):
        try:
            db_session.global_init('sql/db/drons1.sqlite')
            a = self.read_table()

            diction = dict()
            for i in range(len(a)):
                if a[i][0] in diction:
                    diction[a[i][0]] += int(a[i][1])
                else:
                    diction[a[i][0]] = int(a[i][1])

            for item in diction.keys():
                d = request_4.DronsToReq()
                d.dron_name = item
                d.quantity = diction[item]
                d.num = int(self.num_of_request.text())
                session = db_session.create_session()
                session.add(d)
                session.commit()

            d = request_4.RequestDron()
            d.number = int(self.num_of_request.text())
            d.date_create = datetime.date(*self.date_create.date().getDate())
            d.date_close = datetime.date(*self.date_otg.date().getDate())
            if self.check():
                d.state = 'Идет сборка'
            elif self.state.currentText() == 'Создана':
                d.state = 'Запрошено разрешение у ФСБ'
            else:
                d.state = self.state.currentText()
                if self.state.currentText() == 'Готова к отгрузке':
                    self.spis(int(self.num_of_request.text()))

            session = db_session.create_session()
            session.add(d)
            session.commit()

            msg = QMessageBox()
            msg.setWindowTitle("Информация")
            msg.setText("Заявка создана успешно")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()
            if retval == QMessageBox.Ok:
                Session4.close(msg)
        except Exception as e:
            print(e)
            msg = QMessageBox()
            msg.setWindowTitle("Информация")
            msg.setText("Произошла ошибка, возможно вы ввели некорректные данные")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()
            if retval == QMessageBox.Ok:
                Session4.close(msg)


class ListW(QMainWindow, Ui_ListWin):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.create.clicked.connect(self.create_new_request)
        self.change.clicked.connect(self.change_request)
        self.select.clicked.connect(self.selection)

        combo_box_options = []
        db_session.global_init('sql/db/drons1.sqlite')
        session = db_session.create_session()
        nums = []
        for user in session.query(request_4.RequestDron):
            if user.number not in nums:
                combo_box_options.append(f'{user.number}  -   {user.date_create}   -   {user.buyer}')
                nums.append(user.number)
        self.comboBox.clear()
        for t in ["Сортировка по номеру",
                  "Сортировка по дате создания",
                  "Сортировка по дате изменения состояния",
                  "Сортировка по состоянию"]:
            self.comboBox.addItem(t)

    def selection(self):
        self.s = self.comboBox.currentText()
        self.tableWidget.setColumnCount(5)

        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem('N п.п.'))
        self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem('Дата создания'))
        self.tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem('Дата изменения состояния'))
        self.tableWidget.setHorizontalHeaderItem(3, QTableWidgetItem('Состояние'))
        self.tableWidget.setHorizontalHeaderItem(4, QTableWidgetItem('Общая сумма заявки'))

        db_session.global_init('sql/db/drons1.sqlite')
        session = db_session.create_session()
        score = dict()
        for user in session.query(drons_cost.DronCost):
            score[user.name_dron] = user.cost
        a = []
        for user in session.query(request_4.RequestDron):
            s = 0
            for u in session.query(request_4.DronsToReq).filter(request_4.DronsToReq.num == user.number):
                s += int(u.quantity) * int(score[u.dron_name])
            a.append([int(user.id), str(user.date_create), str(user.date_change), user.state, str(s)])
        a.sort(key=lambda x: x[0])
        self.tableWidget.setRowCount(len(a))
        i = 1
        for x in a:
            itm = QTableWidgetItem(f'000{i}')
            itm.setFlags(QtCore.Qt.ItemIsEnabled)

            itm1 = QTableWidgetItem(x[1])
            itm1.setFlags(QtCore.Qt.ItemIsEnabled)

            itm2 = QTableWidgetItem(x[2])
            itm2.setFlags(QtCore.Qt.ItemIsEnabled)

            itm3 = QTableWidgetItem(x[3])
            itm3.setFlags(QtCore.Qt.ItemIsEnabled)

            itm4 = QTableWidgetItem(x[4])
            itm4.setFlags(QtCore.Qt.ItemIsEnabled)

            self.tableWidget.setItem(i - 1, 0, itm)
            self.tableWidget.setItem(i - 1, 1, itm1)
            self.tableWidget.setItem(i - 1, 2, itm2)
            self.tableWidget.setItem(i - 1, 3, itm3)
            self.tableWidget.setItem(i - 1, 4, itm4)

            i += 1

        self.tableWidget.resizeColumnsToContents()
        if self.s == "Сортировка по номеру":
            self.tableWidget.sortItems(0)
        elif self.s == "Сортировка по дате создания":
            self.tableWidget.sortItems(1, QtCore.Qt.DescendingOrder)
        elif self.s == "Сортировка по дате изменения состояния":
            self.tableWidget.sortItems(2, QtCore.Qt.DescendingOrder)
        elif self.s == "Сортировка по состоянию":
            self.tableWidget.sortItems(3, QtCore.Qt.AscendingOrder)

    def create_new_request(self):
        MainWin.show()
        self.close()

    def change_request(self):
        a = int(self.comboBox.currentText().split('  -   ')[0])
        if a:
            MainWin.parameters(a)
            MainWin.show()
            self.close()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Информация")
            msg.setText("Выберите заявку и повторите попытку")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()
            if retval == QMessageBox.Ok:
                Session4.close(msg)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWin = Session4()
    ListW_ = ListW()
    MainWin.show()
    sys.exit(app.exec())
