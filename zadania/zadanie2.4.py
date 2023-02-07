import sys

from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit
from PySide6.QtGui import QAction, QKeySequence


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle('Zadanie2.4')
        self.setFixedSize(QSize(600, 200))

        finallayout = QVBoxLayout()

        self.lineEdit = QLineEdit()
        self.lineEdit.setFixedHeight(50)
        self.lineEdit.setStyleSheet("QLineEdit { font-size: 30px }")
        self.lineEdit.setText("11, 2, 90, -12, 68, 2136, 419, -1")

        finallayout.addWidget(self.lineEdit)

        self.btn = QAction('&Bubble sort', self)
        self.btn.triggered.connect(self.buttonClicked)
        self.btn.setShortcut(QKeySequence('Ctrl+1'))

        self.btn2 = QAction('&Quick sort', self)
        self.btn2.triggered.connect(self.buttonClicked)
        self.btn2.setShortcut(QKeySequence('Ctrl+2'))

        self.btn3 = QAction('&Python sort', self)
        self.btn3.triggered.connect(self.buttonClicked)
        self.btn3.setShortcut(QKeySequence('Ctrl+3'))

        menu = self.menuBar()

        fileMenu = menu.addMenu('&Sort')
        fileMenu.addAction(self.btn)
        fileMenu.addAction(self.btn2)
        fileMenu.addAction(self.btn3)

        widget = QWidget()
        widget.setLayout(finallayout)
        self.setCentralWidget(widget)

    def buttonClicked(self):
        try:
            arr = list(map(int, self.lineEdit.text().replace(' ', '').split(',')))
            buttontext = self.sender().text()
            if buttontext == "&Bubble sort":
                for i in range(len(arr)):
                    for j in range(0, len(arr) - i - 1):
                        if arr[j] > arr[j + 1]:
                            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            elif buttontext == "&Quick sort":
                size = len(arr)
                self.quickSort(arr, 0, size - 1)
            else:
                arr.sort()
            arr = list(map(str, arr))
            self.lineEdit.setText(', '.join(arr))
        except:
            print('error')

    def partition(self, array, low, high):
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= pivot:
                i = i + 1
                (array[i], array[j]) = (array[j], array[i])
        (array[i + 1], array[high]) = (array[high], array[i + 1])
        return i + 1

    def quickSort(self, array, low, high):
        if low < high:
            pi = self.partition(array, low, high)
            self.quickSort(array, low, pi - 1)
            self.quickSort(array, pi + 1, high)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()