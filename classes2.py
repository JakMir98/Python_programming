#!/usr/bin/env python3

import classes1 as complex
import os
import sys
import math
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QLCDNumber, QMessageBox, QRadioButton, QHBoxLayout, QGridLayout, QGroupBox, QVBoxLayout


class myQLineEdit(QLineEdit):
    clicked = pyqtSignal()

    def __init__(self, widget):
        super().__init__(widget)

    def mousePressEvent(self, QMouseEvent):
        self.clicked.emit()


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Complex calc"
        self.left = 100
        self.top = 100
        self.width = 320
        self.height = 400
        self.buttonSize = 50
        self.initUI()
        self.complexNum = complex.Complex()
        self.firstActive = True
        self.action = '+'

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.add_btn = QPushButton('&+', self)
        self.add_btn.setToolTip('Dodawanie')
        self.add_btn.clicked.connect(self.on_click_dodawanie)

        self.sub_btn = QPushButton('&-', self)
        self.sub_btn.setToolTip('Odejmowanie')
        self.sub_btn.clicked.connect(self.on_click_odejmowanie)

        self.mul_btn = QPushButton('&*', self)
        self.mul_btn.setToolTip('Mnozenie')
        self.mul_btn.clicked.connect(self.on_click_mnozenie)

        self.div_btn = QPushButton('&/', self)
        self.div_btn.setToolTip('Dzielenie')
        self.div_btn.clicked.connect(self.on_click_dzielenie)

        self.result_btn = QPushButton('&=', self)
        self.result_btn.setToolTip('Wynik')
        self.result_btn.clicked.connect(self.on_click_result)

        self.reset_btn = QPushButton('&C', self)
        self.reset_btn.setToolTip('reset')
        self.reset_btn.clicked.connect(self.on_click_reset)

        self.zero_btn = QPushButton('&0', self)
        self.zero_btn.clicked.connect(self.on_click0)

        self.one_btn = QPushButton('1', self)
        self.one_btn.clicked.connect(self.on_click1)

        self.two_btn = QPushButton('2', self)
        self.two_btn.clicked.connect(self.on_click2)

        self.three_btn = QPushButton('3', self)
        self.three_btn.clicked.connect(self.on_click3)

        self.four_btn = QPushButton('4', self)
        self.four_btn.clicked.connect(self.on_click4)

        self.five_btn = QPushButton('5', self)
        self.five_btn.clicked.connect(self.on_click5)

        self.six_btn = QPushButton('6', self)
        self.six_btn.clicked.connect(self.on_click6)

        self.seven_btn = QPushButton('7', self)
        self.seven_btn.clicked.connect(self.on_click7)

        self.eight_btn = QPushButton('8', self)
        self.eight_btn.clicked.connect(self.on_click8)

        self.nine_btn = QPushButton('9', self)
        self.nine_btn.clicked.connect(self.on_click9)

        self.label1 = QLabel('Real part: ', self)

        self.realPartTB = myQLineEdit(self)
        self.realPartTB.resize(280, 40)
        self.realPartTB.setText('')
        self.realPartTB.clicked.connect(self.press1)
        self.realPartTB.setFocus()

        self.label2 = QLabel('Imaginary part: ', self)

        self.imagPartTB = myQLineEdit(self)
        self.imagPartTB.resize(280, 40)
        self.imagPartTB.setText('')
        self.imagPartTB.clicked.connect(self.press2)

        self.label3 = QLabel('Result: ', self)

        self.textbox3 = QLineEdit(self)
        self.textbox3.resize(280, 40)
        self.textbox3.setText('')
        self.textbox3.setReadOnly(True)

        self.groupBox1 = QGroupBox()
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.addWidget(self.label1)
        self.verticalLayout.addWidget(self.realPartTB)
        self.verticalLayout.addWidget(self.label2)
        self.verticalLayout.addWidget(self.imagPartTB)
        self.verticalLayout.addWidget(self.label3)
        self.verticalLayout.addWidget(self.textbox3)
        self.groupBox1.setLayout(self.verticalLayout)

        self.groupBox2 = QGroupBox()
        self.layout = QGridLayout()
        self.layout.setColumnStretch(0, 2)
        self.layout.setColumnStretch(1, 2)
        self.layout.setColumnStretch(2, 2)
        self.layout.setColumnStretch(3, 2)

        self.layout.addWidget(self.add_btn, 0, 0)
        self.layout.addWidget(self.sub_btn, 0, 1)
        self.layout.addWidget(self.mul_btn, 0, 2)
        self.layout.addWidget(self.div_btn, 0, 3)
        self.layout.addWidget(self.result_btn, 1, 0)
        self.layout.addWidget(self.reset_btn, 1, 1)
        self.layout.addWidget(self.zero_btn, 1, 2)
        self.layout.addWidget(self.one_btn, 1, 3)
        self.layout.addWidget(self.two_btn, 2, 0)
        self.layout.addWidget(self.three_btn, 2, 1)
        self.layout.addWidget(self.four_btn, 2, 2)
        self.layout.addWidget(self.five_btn, 2, 3)
        self.layout.addWidget(self.six_btn, 3, 0)
        self.layout.addWidget(self.seven_btn, 3, 1)
        self.layout.addWidget(self.eight_btn, 3, 2)
        self.layout.addWidget(self.nine_btn, 3, 3)
        self.groupBox2.setLayout(self.layout)

        self.windowLayout = QVBoxLayout()
        self.windowLayout.addWidget(self.groupBox1)
        self.windowLayout.addWidget(self.groupBox2)
        self.setLayout(self.windowLayout)

        self.show()

    def press1(self):
        self.firstActive = True

    def press2(self):
        self.firstActive = False

    def clearEditText(self):
        self.textbox3.setText(str(self.complexNum))
        self.realPartTB.clear()
        self.imagPartTB.clear()

    @pyqtSlot()
    def on_click_dodawanie(self):
        try:
            if self.complexNum != complex.Complex():
                secondOp = complex.Complex(
                    float(self.realPartTB.text()), float(self.imagPartTB.text()))
                self.complexNum = self.complexNum + secondOp
            else:
                self.complexNum = complex.Complex(
                    float(self.realPartTB.text()), float(self.imagPartTB.text()))
            self.clearEditText()
            self.action = '+'
        except ValueError:
            QMessageBox.warning(self, "Blad", "Bledne dane", QMessageBox.Ok)

    def on_click_odejmowanie(self):
        try:
            if self.complexNum != complex.Complex():
                secondOp = complex.Complex(
                    float(self.realPartTB.text()), float(self.imagPartTB.text()))
                self.complexNum = self.complexNum - secondOp
            else:
                self.complexNum = complex.Complex(
                    float(self.realPartTB.text()), float(self.imagPartTB.text()))
            self.clearEditText()
            self.action = '-'
        except ValueError:
            QMessageBox.warning(self, "Blad", "Bledne dane", QMessageBox.Ok)

    def on_click_mnozenie(self):
        try:
            if self.complexNum != complex.Complex():
                secondOp = complex.Complex(
                    float(self.realPartTB.text()), float(self.imagPartTB.text()))
                self.complexNum = self.complexNum * secondOp
            else:
                self.complexNum = complex.Complex(
                    float(self.realPartTB.text()), float(self.imagPartTB.text()))
            self.clearEditText()
            self.action = '*'
        except ValueError:
            QMessageBox.warning(self, "Blad", "Bledne dane", QMessageBox.Ok)

    def on_click_dzielenie(self):
        try:
            if self.complexNum != complex.Complex():
                secondOp = complex.Complex(
                    float(self.realPartTB.text()), float(self.imagPartTB.text()))
                self.complexNum = self.complexNum / secondOp
            else:
                self.complexNum = complex.Complex(
                    float(self.realPartTB.text()), float(self.imagPartTB.text()))
            self.clearEditText()
            self.action = '/'
        except ValueError:
            QMessageBox.warning(self, "Blad", "Bledne dane", QMessageBox.Ok)

    def on_click_result(self):
        try:
            secondOp = complex.Complex(
                float(self.realPartTB.text()), float(self.imagPartTB.text()))
            if self.action == '+':
                self.complexNum = self.complexNum + secondOp
            elif self.action == '-':
                self.complexNum = self.complexNum - secondOp
            elif self.action == '*':
                self.complexNum = self.complexNum * secondOp
            elif self.action == '/':
                self.complexNum = self.complexNum / secondOp
            self.textbox3.setText(str(self.complexNum))
        except ValueError:
            QMessageBox.warning(self, "Blad", "Bledne dane", QMessageBox.Ok)

    def on_click_reset(self):
        self.complexNum = complex.Complex()
        self.realPartTB.clear()
        self.imagPartTB.clear()
        self.textbox3.clear()

    def on_click0(self):
        if self.firstActive == True:
            if self.realPartTB.text() != '':
                schowek = self.realPartTB.text()
                schowek += '0'
                self.realPartTB.setText(schowek)
            else:
                self.realPartTB.setText('0')
        else:
            if self.imagPartTB.text() != '':
                schowek = self.imagPartTB.text()
                schowek += '0'
                self.imagPartTB.setText(schowek)
            else:
                self.imagPartTB.setText('0')

    def on_click1(self):
        if self.firstActive == True:
            if self.realPartTB.text() != '':
                schowek = self.realPartTB.text()
                schowek += '1'
                self.realPartTB.setText(schowek)
            else:
                self.realPartTB.setText('1')
        else:
            if self.imagPartTB.text() != '':
                schowek = self.imagPartTB.text()
                schowek += '1'
                self.imagPartTB.setText(schowek)
            else:
                self.imagPartTB.setText('1')

    def on_click2(self):
        if self.firstActive == True:
            if self.realPartTB.text() != '':
                schowek = self.realPartTB.text()
                schowek += '2'
                self.realPartTB.setText(schowek)
            else:
                self.realPartTB.setText('2')
        else:
            if self.imagPartTB.text() != '':
                schowek = self.imagPartTB.text()
                schowek += '2'
                self.imagPartTB.setText(schowek)
            else:
                self.imagPartTB.setText('2')

    def on_click3(self):
        if self.firstActive == True:
            if self.realPartTB.text() != '':
                schowek = self.realPartTB.text()
                schowek += '3'
                self.realPartTB.setText(schowek)
            else:
                self.realPartTB.setText('3')
        else:
            if self.imagPartTB.text() != '':
                schowek = self.imagPartTB.text()
                schowek += '3'
                self.imagPartTB.setText(schowek)
            else:
                self.imagPartTB.setText('3')

    def on_click4(self):
        if self.firstActive == True:
            if self.realPartTB.text() != '':
                schowek = self.realPartTB.text()
                schowek += '4'
                self.realPartTB.setText(schowek)
            else:
                self.realPartTB.setText('4')
        else:
            if self.imagPartTB.text() != '':
                schowek = self.imagPartTB.text()
                schowek += '4'
                self.imagPartTB.setText(schowek)
            else:
                self.imagPartTB.setText('4')

    def on_click5(self):
        if self.firstActive == True:
            if self.realPartTB.text() != '':
                schowek = self.realPartTB.text()
                schowek += '5'
                self.realPartTB.setText(schowek)
            else:
                self.realPartTB.setText('5')
        else:
            if self.imagPartTB.text() != '':
                schowek = self.imagPartTB.text()
                schowek += '5'
                self.imagPartTB.setText(schowek)
            else:
                self.imagPartTB.setText('5')

    def on_click6(self):
        if self.firstActive == True:
            if self.realPartTB.text() != '':
                schowek = self.realPartTB.text()
                schowek += '6'
                self.realPartTB.setText(schowek)
            else:
                self.realPartTB.setText('6')
        else:
            if self.imagPartTB.text() != '':
                schowek = self.imagPartTB.text()
                schowek += '6'
                self.imagPartTB.setText(schowek)
            else:
                self.imagPartTB.setText('6')

    def on_click7(self):
        if self.firstActive == True:
            if self.realPartTB.text() != '':
                schowek = self.realPartTB.text()
                schowek += '7'
                self.realPartTB.setText(schowek)
            else:
                self.realPartTB.setText('7')
        else:
            if self.imagPartTB.text() != '':
                schowek = self.imagPartTB.text()
                schowek += '7'
                self.imagPartTB.setText(schowek)
            else:
                self.imagPartTB.setText('7')

    def on_click8(self):
        if self.firstActive == True:
            if self.realPartTB.text() != '':
                schowek = self.realPartTB.text()
                schowek += '8'
                self.realPartTB.setText(schowek)
            else:
                self.realPartTB.setText('8')
        else:
            if self.imagPartTB.text() != '':
                schowek = self.imagPartTB.text()
                schowek += '8'
                self.imagPartTB.setText(schowek)
            else:
                self.imagPartTB.setText('8')

    def on_click9(self):
        if self.firstActive == True:
            if self.realPartTB.text() != '':
                schowek = self.realPartTB.text()
                schowek += '9'
                self.realPartTB.setText(schowek)
            else:
                self.realPartTB.setText('9')
        else:
            if self.imagPartTB.text() != '':
                schowek = self.imagPartTB.text()
                schowek += '9'
                self.imagPartTB.setText(schowek)
            else:
                self.imagPartTB.setText('9')


if __name__ == '__main__':
    script_dir = os.path.dirname(__file__)
    abs_file_path_read = os.path.join(script_dir, "pic.png")
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(abs_file_path_read))
    ex = App()
    sys.exit(app.exec_())
