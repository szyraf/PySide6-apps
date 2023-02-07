from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('sloty')

        # self.setFixedSize(QSize(500, 100))
        self.setMinimumSize(QSize(200, 200))
        self.setMaximumSize(QSize(500, 500))

        self.buttonChecked = True

        self.button = QPushButton('click aaaaaa')
        self.button.setCheckable(True)
        self.button.clicked.connect(self.buttonClicked)
        self.button.clicked.connect(self.buttonToggled)
        self.button.released.connect(self.buttonReleased)
        self.button.setChecked(self.buttonChecked)
        self.setCentralWidget(self.button)

    def buttonClicked(self):
        print('kliku kliku')

    def buttonToggled(self, checked):
        print(checked)

    def buttonReleased(self):
        self.buttonChecked = self.button.isChecked()
        print(self.buttonChecked)




app = QApplication()
window = MainWindow()
window.show()

app.exec()