from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QComboBox
from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel, QMessageBox
import sys
from ecxel_example import *
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
import datetime
from PyQt5 import QtCore
from sql.data.__all_models import *


class UiMainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.size_table = 1
        self.last_table_update = []


    def initUI(self):
        self.setGeometry(200, 200, 720, 600)
        self.setWindowTitle("Session2")
        self.number = 1
        self.date = 2
        self.size_table = 10

        self.pushButton_add = QPushButton("+", self)
        self.pushButton_add.resize(50, 50)
        self.pushButton_add.move(660, 500)
        self.pushButton_add.clicked.connect(self.add_stroka)

        self.pushButton_ok = QPushButton("Ok", self)
        self.pushButton_ok.resize(100, 50)
        self.pushButton_ok.move(10, 520)
        self.pushButton_ok.clicked.connect(self.ok)

        self.pushButton_download = QPushButton("Записать", self)
        self.pushButton_download.resize(100, 50)
        self.pushButton_download.move(130, 520)
        self.pushButton_download.clicked.connect(self.write)

        self.pushButton_open_file2 = QPushButton("Закрыть", self)
        self.pushButton_open_file2.resize(100, 50)
        self.pushButton_open_file2.move(250, 520)
        self.pushButton_open_file2.clicked.connect(self.closing)

        self.lineEdit_otvetstv = QLineEdit('', self)
        self.lineEdit_otvetstv.setPlaceholderText("")
        self.lineEdit_otvetstv.resize(200, 20)
        self.lineEdit_otvetstv.move(190, 50)
        self.lineEdit_otvetstv.setObjectName("lineEdit")

        self.drons = QLabel(self)
        self.drons.setText(f"Поступление комплектующих № 000{self.number} от {datetime.datetime.today().strftime('%d.%m.%Y')}")
        self.drons.move(10, 20)

        self.komplecktushie = QLabel(self)
        self.komplecktushie.setText("Ответственный за прием:")
        self.komplecktushie.move(10, 50)

        self.tableWidget_komplectuyshie = QTableWidget(self)
        self.tableWidget_komplectuyshie.setColumnCount(3)
        self.tableWidget_komplectuyshie.move(10, 100)
        self.tableWidget_komplectuyshie.resize(700, 400)
        self.tableWidget_komplectuyshie.setHorizontalHeaderItem(0, QTableWidgetItem('Комплектующее'))
        self.tableWidget_komplectuyshie.setHorizontalHeaderItem(1, QTableWidgetItem('Серийный номер'))
        self.tableWidget_komplectuyshie.setHorizontalHeaderItem(2, QTableWidgetItem('Количество'))
        self.upload()

    def upload(self):
        combo_box_options = []
        db_session.global_init('sql/db/drons1.sqlite')
        session = db_session.create_session()
        for user in session.query(details.DetailCategory):
            combo_box_options.append(user.name_det)
        self.tableWidget_komplectuyshie.setRowCount(1)

        item1 = QTableWidgetItem('')
        self.tableWidget_komplectuyshie.setItem(0, 1, item1)
        item2 = QTableWidgetItem('')
        self.tableWidget_komplectuyshie.setItem(0, 2, item2)
        combo = QComboBox()
        for t in combo_box_options:
            combo.addItem(t)
        self.tableWidget_komplectuyshie.setCellWidget(0, 0, combo)

    def ok(self):
        pass

    def write(self):
        a = self.read_table()
        db_session.global_init('/Users/gavrishekaterina/PycharmProjects/olimp3-master/app/drons1.sqlite')
        print(a)
        for i in range(len(a)):
            b = balance.Balance()
            b.name_det = a[i][0]
            b.quantity = int(a[i][2])
            b.date = datetime.datetime.today()
            session = db_session.create_session()
            session.add(b)
            session.commit()

    def add_stroka(self):
        combo_box_options = []
        db_session.global_init('sql/db/drons1.sqlite')
        session = db_session.create_session()
        for user in session.query(details.DetailCategory):
            combo_box_options.append(user.name_det)
        self.tableWidget_komplectuyshie.setRowCount(self.size_table + 1)
        itm = QTableWidgetItem(str(''))
        combo = QComboBox()
        for t in combo_box_options:
            combo.addItem(t)
        self.tableWidget_komplectuyshie.setCellWidget(self.size_table, 0, combo)
        self.tableWidget_komplectuyshie.setItem(self.size_table, 1, itm)
        itm1 = QTableWidgetItem(str(''))
        self.tableWidget_komplectuyshie.setItem(self.size_table, 2, itm1)
        self.size_table += 1
        self.tableWidget_komplectuyshie.resizeColumnsToContents()

    def closing(self):
        if self.last_table_update == self.read_table():
            UiMainWindow.close(self)
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Информация")
            msg.setText("Есть несохранённые изменения")
            # msg.setInformativeText(f"{message1}\n{message2}\n{message3}")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            retval = msg.exec_()
            if retval == QMessageBox.Ok:
                UiMainWindow.close(self)

    def read_table(self):
        # эта функция возвращает данные таблицы
        # список состоит из списков,  вот так:
        # [["комплектющее", "серийный номер", "количество"], ["комплектющее", "серийный номер", "количество"]]
        info_table = []
        for i in range(self.size_table):
            a = []
            for j in range(3):
                if j != 0:
                    a.append(self.tableWidget_komplectuyshie.item(i, j).text())
                else:
                    a.append(self.tableWidget_komplectuyshie.cellWidget(i, j).currentText())
            info_table.append(a)
        return info_table


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = UiMainWindow()
    MainWindow.show()
    sys.exit(app.exec())