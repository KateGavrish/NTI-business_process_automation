from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QComboBox
from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel, QMessageBox
import sys
from ecxel_example import *
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QCheckBox
from PyQt5 import QtCore


class UiMainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setGeometry(200, 200, 720, 600)
        self.setWindowTitle("Session2")
        self.number = 1
        self.date = 2

        self.pushButton_ok = QPushButton("Ok", self)
        self.pushButton_ok.resize(100, 50)
        self.pushButton_ok.move(10, 520)
        self.pushButton_ok.clicked.connect(self.ok)

        self.pushButton_download = QPushButton("Записать", self)
        self.pushButton_download.resize(100, 50)
        self.pushButton_download.move(130, 520)
        self.pushButton_download.clicked.connect(self.zapisat)

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
        self.drons.setText(f"Поступление комплектующих {self.number} от {self.date}")
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

    def ok(self):
        pass

    def zapisat(self):
        pass

    def closing(self):
        UiMainWindow.close(self)

    def update_table(self, spisok):
        # список состоит из списков,  вот так:
        # [["комплектющее", "серийный номер", "количество"], ["комплектющее", "серийный номер", "количество"]]
        self.tableWidget_komplectuyshie.setRowCount(len(spisok))
        for i in range(len(spisok)):
            for j in range(3):
                itm = QTableWidgetItem(str(spisok[i][j]))
                itm.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget_komplectuyshie.setItem(i, j, itm)
        self.tableWidget_komplectuyshie.resizeColumnsToContents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = UiMainWindow()
    MainWindow.show()
    sys.exit(app.exec())