from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PySide6.QtCore import QSize
import random

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('mysz')

        # self.setFixedSize(QSize(500, 100))
        self.setMinimumSize(QSize(300, 300))
        self.setMaximumSize(QSize(500, 500))

        self.label = QLabel('wrrrrrrr')
        self.setCentralWidget(self.label)
        self.setMouseTracking(True)

    def mouseMoveEvent(self, e):
        self.label.setText('mysz! szczury! papugi!')
        self.setMouseTracking(False)

    def mousePressEvent(self, e):
        self.label.setText('Ała! Nie atakuj!')

    def mouseReleaseEvent(self, e):
        self.label.setText('zwolniono')

    def mouseDoubleClickEvent(self, e):
        self.label.setText('Double Kill!')


app = QApplication()
window = MainWindow()
window.show()

app.exec()