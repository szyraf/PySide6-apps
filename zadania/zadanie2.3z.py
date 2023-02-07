import sys

from PySide6 import QtCore
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QLineEdit, QPushButton
from PySide6.QtGui import QPalette, QColor, QDoubleValidator
import math


class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle('Zadanie2.3')
        self.setFixedSize(QSize(300, 500))

        finallayout = QVBoxLayout()

        self.lineEdit = QLineEdit()
        self.lineEdit.setFixedHeight(50)
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight)
        self.lineEdit.setStyleSheet("QLineEdit { font-size: 30px }")
        self.lineEdit.setText("0")
        self.lineEdit.textChanged.connect(self.textChanged)

        validator = QDoubleValidator()
        self.lineEdit.setValidator(validator)

        finallayout.addWidget(self.lineEdit)

        layout = QGridLayout()

        buttons = [
            ["", "CE", "C", "⌫"],
            ["1/x", "x²", "√x", "÷"],
            ["7", "8", "9", "×"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["+/-", "0", ",", "="],
        ]

        for y in range(6):
            for x in range(4):
                self.btn = QPushButton(buttons[y][x])
                self.btn.clicked.connect(self.buttonClicked)
                self.btn.setFixedHeight(50)
                layout.addWidget(self.btn, y, x)

        finallayout.addLayout(layout)

        widget = QWidget()
        widget.setLayout(finallayout)
        self.setCentralWidget(widget)

        self.remeberNumber = 0
        self.remeberSign = ""

    def textChanged(self, s):
        if s == "":
            self.lineEdit.setText("0")
        elif s == "-0":
            self.lineEdit.setText("0")
        elif s[0] == ",":
            self.lineEdit.setText(s[1:])
        elif len(s) > 1:
            if s[0] == "0" and s[1] != ",":
                self.lineEdit.setText(s[1:])

    def buttonClicked(self):
        buttontext = self.sender().text()

        try:
            if 0 <= int(buttontext) <= 9:
                self.lineEdit.setText(self.lineEdit.text() + buttontext)
        except ValueError:
            if buttontext == ",":
                if "," not in self.lineEdit.text() and self.lineEdit.text() != "":
                    self.lineEdit.setText(self.lineEdit.text() + ",")
            elif buttontext == "CE" or buttontext == "C":
                self.lineEdit.setText("0")
                self.remeberNumber = 0
                self.remeberSign = ""
            elif buttontext == "⌫":
                self.lineEdit.setText(self.lineEdit.text()[:-1])
            elif buttontext == "x²":
                self.lineEdit.setText(
                    self.makeGood(str(self.lineEditToFloat() * self.lineEditToFloat()).replace(".", ",")))
            elif buttontext == "√x":
                if self.lineEditToFloat() >= 0:
                    self.lineEdit.setText(self.makeGood(str(math.sqrt(self.lineEditToFloat())).replace(".", ",")))
            elif buttontext == "1/x":
                if self.lineEditToFloat() != 0:
                    self.lineEdit.setText(self.makeGood(str(1 / self.lineEditToFloat()).replace(".", ",")))
            elif buttontext == "+/-":
                self.lineEdit.setText(self.makeGood(str(-self.lineEditToFloat()).replace(".", ",")))
            elif buttontext == "+" or buttontext == "-" or buttontext == "×" or buttontext == "÷":
                self.remeberNumber = self.lineEditToFloat()
                self.remeberSign = buttontext
                self.lineEdit.setText("0")
            elif buttontext == "=":
                if self.remeberSign == "+":
                    self.lineEdit.setText(
                        self.makeGood(str(self.remeberNumber + self.lineEditToFloat()).replace(".", ",")))
                elif self.remeberSign == "-":
                    self.lineEdit.setText(
                        self.makeGood(str(self.remeberNumber - self.lineEditToFloat()).replace(".", ",")))
                    self.remeberNumber = 0
                    self.remeberSign = ""
                elif self.remeberSign == "×":
                    self.lineEdit.setText(
                        self.makeGood(str(self.remeberNumber * self.lineEditToFloat()).replace(".", ",")))
                elif self.remeberSign == "÷":
                    if self.lineEditToFloat() != 0:
                        self.lineEdit.setText(
                            self.makeGood(str(self.remeberNumber / self.lineEditToFloat()).replace(".", ",")))
                        self.remeberNumber = 0
                        self.remeberSign = ""

    def lineEditToFloat(self):
        if self.lineEdit.text()[len(self.lineEdit.text()) - 1] == ",":
            self.lineEdit.setText(self.lineEdit.text()[:-1])
        return float(self.lineEdit.text().replace(",", "."))

    def makeGood(self, s):
        x = s.find(",")
        if x != -1:
            if len(s) == x + 2:
                if s[x + 1] == "0":
                    return s[:-2]
        return s


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
