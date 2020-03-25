from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QComboBox
from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel, QMessageBox
import sys
from ecxel_example import *


class UiMainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 400, 600, 300)
        self.setWindowTitle("Session1")

        self.pushButton_download = QPushButton("Загрузить", self)
        self.pushButton_download.resize(100, 50)
        self.pushButton_download.move(10, 120)
        self.pushButton_download.clicked.connect(self.download)

        self.pushButton_open_file2 = QPushButton("Закрыть", self)
        self.pushButton_open_file2.resize(100, 50)
        self.pushButton_open_file2.move(130, 120)
        self.pushButton_open_file2.clicked.connect(self.closing)

        self.pushButton_open_file1 = QPushButton("...", self)
        self.pushButton_open_file1.resize(40, 30)
        self.pushButton_open_file1.move(470, 16)
        self.pushButton_open_file1.clicked.connect(self.open_path1)

        self.pushButton_open_file2 = QPushButton("...", self)
        self.pushButton_open_file2.resize(40, 30)
        self.pushButton_open_file2.move(470, 46)
        self.pushButton_open_file2.clicked.connect(self.open_path2)

        self.pushButton_open_file3 = QPushButton("...", self)
        self.pushButton_open_file3.resize(40, 30)
        self.pushButton_open_file3.move(470, 76)
        self.pushButton_open_file3.clicked.connect(self.open_path3)

        self.lineEdit_drons = QLineEdit('', self)
        self.lineEdit_drons.setPlaceholderText("Выбор файла")
        self.lineEdit_drons.resize(300, 20)
        self.lineEdit_drons.move(160, 20)
        self.lineEdit_drons.setObjectName("lineEdit")

        self.lineEdit_komplecktushie = QLineEdit('', self)
        self.lineEdit_komplecktushie.setPlaceholderText("Выбор файла")
        self.lineEdit_komplecktushie.resize(300, 20)
        self.lineEdit_komplecktushie.move(160, 50)
        self.lineEdit_komplecktushie.setObjectName("lineEdit")

        self.lineEdit_technial_maps = QLineEdit('', self)
        self.lineEdit_technial_maps.setPlaceholderText("Выбор файла")
        self.lineEdit_technial_maps.resize(300, 20)
        self.lineEdit_technial_maps.move(160, 80)
        self.lineEdit_technial_maps.setObjectName("lineEdit")

        self.drons = QLabel(self)
        self.drons.setText("Дроны")
        self.drons.move(10, 20)

        self.komplecktushie = QLabel(self)
        self.komplecktushie.setText("Комплектующие")
        self.komplecktushie.move(10, 50)

        self.technial_maps = QLabel(self)
        self.technial_maps.setText("Тех. карты")
        self.technial_maps.move(10, 80)

    def open_path1(self):
        filename = QFileDialog.getOpenFileName(self, 'Open file', None, "(*.xlsx)")[0]
        self.lineEdit_drons.setText(filename)

    def open_path2(self):
        filename = QFileDialog.getOpenFileName(self, 'Open file', None, "(*.xlsx)")[0]
        self.lineEdit_komplecktushie.setText(filename)

    def open_path3(self):
        filename = QFileDialog.getOpenFileName(self, 'Open file', None, "(*.xlsx)")[0]
        self.lineEdit_technial_maps.setText(filename)

    def download(self):
        filename1 = self.lineEdit_drons.text()
        filename2 = self.lineEdit_komplecktushie.text()
        filename3 = self.lineEdit_technial_maps.text()
        message1 = ""
        message2 = ""
        message3 = ""
        ok1 = True
        ok2 = True
        ok3 = True
        try:
            drons = import_drons(filename1)
            message1 = "Загрузка информации о дронах прошла успешно"
        except:
            message1 = "При загрузке информации о дронах возникла ошибка"
            ok1 = False
        try:
            komplectuyshye = import_komplecktuyshye(filename2)
            message2 = "Загрузка информации о комплектующих прошла успешно"
        except:
            ok2 = False
            message2 = "При загрузке информации о комплектующих возникла ошибка"
        try:
            technial_maps = import_technial_map(filename3)
            message3 = "Загрузке информации о технических картах прошла успешно"
        except:
            ok3 = False
            message3 = "При загрузке информации о технических картах возникла ошибка"
        if ok1 and ok2 and ok3:
            mes = "Загрузка прошла успешно"
        else:
            mes = "При загрузке произошли некоторые ошибки"
        msg = QMessageBox()
        msg.setWindowTitle("Информация")
        msg.setText(mes)
        msg.setInformativeText(f"{message1}\n{message2}\n{message3}")
        result = msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()

    def closing(self):
        UiMainWindow.close(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = UiMainWindow()
    MainWindow.show()
    sys.exit(app.exec())