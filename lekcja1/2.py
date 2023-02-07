from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('app')

        # self.setFixedSize(QSize(500, 100))

        self.setMinimumSize(QSize(200, 200))
        self.setMaximumSize(QSize(500, 500))

        button = QPushButton('click aaaaaa')
        self.setCentralWidget(button)

app = QApplication()
window = MainWindow()
window.show()

app.exec()