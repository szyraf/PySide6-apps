import math
import sys

from PySide6 import QtGui
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow
from MainWindow import Ui_MainWindow
from Wykresy import Ui_Form
from PySide6.QtGui import QDoubleValidator

class Wykresy(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(Wykresy, self).__init__(parent)
        self.setupUi(self)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.lineEdit.textChanged.connect(self.textChanged)

        validator = QDoubleValidator()
        self.lineEdit.setValidator(validator)

        self.pushButton.pressed.connect(self.buttonClicked)
        for i in range(2, 29):
            eval('self.pushButton_' + str(i) + '.pressed.connect(self.buttonClicked)')

        self.remeberNumber = 0
        self.remeberNumber2 = 0
        self.remeberSign = ""

        self.dialog = Wykresy(self)


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
        buttontext = str(self.sender().text())

        try:
            if 0 <= int(buttontext) <= 9:
                self.lineEdit.setText(self.lineEdit.text() + buttontext)
        except ValueError:
            if buttontext == ",":
                if "," not in self.lineEdit.text() and self.lineEdit.text() != "":
                    self.lineEdit.setText(self.lineEdit.text() + ",")
            elif buttontext == "wykresy":
                self.dialog.show()
            elif buttontext == "sin" or buttontext == "cos" or buttontext == "tg" or buttontext == "ctg":
                if buttontext == "sin":
                    self.lineEdit.setText(self.makeGood(str("{:.7f}".format(math.sin(self.lineEditToFloat()))).replace(".", ",")))
                if buttontext == "cos":
                    self.lineEdit.setText(self.makeGood(str("{:.7f}".format(math.cos(self.lineEditToFloat()))).replace(".", ",")))
                if buttontext == "tg":
                    self.lineEdit.setText(self.makeGood(str("{:.7f}".format(math.tan(self.lineEditToFloat()))).replace(".", ",")))
                if buttontext == "ctg":
                    if (math.tan(self.lineEditToFloat()) != 0):
                        self.lineEdit.setText(self.makeGood(str("{:.7f}".format(1 / math.tan(self.lineEditToFloat()))).replace(".", ",")))
            elif buttontext == "CE" or buttontext == "C":
                self.lineEdit.setText("0")
                self.remeberNumber = 0
                self.remeberSign = ""
                self.remeberNumber2 = 0
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
                self.remeberNumber2 = 0
            elif buttontext == "=":
                if self.remeberNumber2 == 0:
                    self.remeberNumber2 = self.lineEditToFloat()

                    if self.remeberSign == "+":
                        self.lineEdit.setText(
                            self.makeGood(str(self.remeberNumber + self.remeberNumber2).replace(".", ",")))
                    elif self.remeberSign == "-":
                        self.lineEdit.setText(
                            self.makeGood(str(self.remeberNumber - self.remeberNumber2).replace(".", ",")))
                    elif self.remeberSign == "×":
                        self.lineEdit.setText(
                            self.makeGood(str(self.remeberNumber * self.remeberNumber2).replace(".", ",")))
                    elif self.remeberSign == "÷":
                        if self.lineEditToFloat() != 0:
                            self.lineEdit.setText(
                                self.makeGood(str(self.remeberNumber / self.remeberNumber2).replace(".", ",")))
                else:
                    if self.remeberSign == "+":
                        self.lineEdit.setText(
                            self.makeGood(str(self.lineEditToFloat() + self.remeberNumber2).replace(".", ",")))
                    elif self.remeberSign == "-":
                        self.lineEdit.setText(
                            self.makeGood(str(self.lineEditToFloat() - self.remeberNumber2).replace(".", ",")))
                    elif self.remeberSign == "×":
                        self.lineEdit.setText(
                            self.makeGood(str(self.lineEditToFloat() * self.remeberNumber2).replace(".", ",")))
                    elif self.remeberSign == "÷":
                        if self.lineEditToFloat() != 0:
                            self.lineEdit.setText(
                                self.makeGood(str(self.lineEditToFloat() / self.remeberNumber2).replace(".", ",")))

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
w = MainWindow()
app.exec()