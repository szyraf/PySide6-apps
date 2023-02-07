import sys

from PySide6 import QtCore
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QLineEdit, QPushButton
from PySide6.QtGui import QPalette, QColor, QDoubleValidator


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

        self.setWindowTitle('Zadanie2.2')
        self.setFixedSize(QSize(300, 500))

        finallayout = QVBoxLayout()

        self.lineEdit = QLineEdit()
        self.lineEdit.setPlaceholderText('')
        self.lineEdit.setFixedHeight(50)
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight)
        self.lineEdit.setStyleSheet("QLineEdit { font-size: 30px }")

        validator = QDoubleValidator()
        self.lineEdit.setValidator(validator)

        finallayout.addWidget(self.lineEdit)

        layout = QGridLayout()

        buttons = [
            ["%", "CE", "C", "⌫"],
            ["1/x", "x^2", "√x", "/"],
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

    def buttonClicked(self):
        buttontext = self.sender().text()
        print(buttontext)

        try:
            if 0 <= int(buttontext) <= 9:
                self.lineEdit.setText(self.lineEdit.text() + buttontext)
        except ValueError as verr:
            if buttontext == ",":
                if "," not in self.lineEdit.text():
                    self.lineEdit.setText(self.lineEdit.text() + ",")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
