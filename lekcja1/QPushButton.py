from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import QSize
import random

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('sloty')

        # self.setFixedSize(QSize(500, 100))
        self.setMinimumSize(QSize(300, 300))
        self.setMaximumSize(QSize(500, 500))


        self.button = QPushButton('Zmień tytuł')
        self.button.setCheckable(True)

        self.button.clicked.connect(self.buttonClicked)

        self.setCentralWidget(self.button)

    def buttonClicked(self):
        okno = random.randint(0, 100)
        if okno == 0:
            self.button.setText('ała, bolało')
            self.button.setEnabled(False)
            self.setWindowTitle("ERROR 404")
        else:
            self.setWindowTitle('Okno ' + str(okno))



app = QApplication()
window = MainWindow()
window.show()

app.exec()