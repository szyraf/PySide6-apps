from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('sloty')

        # self.setFixedSize(QSize(500, 100))
        self.setMinimumSize(QSize(200, 200))
        self.setMaximumSize(QSize(500, 500))


        self.button = QPushButton('click aaaaaa')
        self.button.setCheckable(True)

        self.button.clicked.connect(self.buttonClicked)

        self.setCentralWidget(self.button)

    def buttonClicked(self):
        self.button.setText('ała, bolało')
        self.button.setEnabled(False)

        self.setWindowTitle("ERROR 404")






app = QApplication()
window = MainWindow()
window.show()

app.exec()