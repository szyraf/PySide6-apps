from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QCheckBox, QComboBox, QDateEdit, QDateTimeEdit,
                               QDial, QDoubleSpinBox, QFontComboBox, QLabel, QLCDNumber, QLineEdit, QProgressBar,
                               QPushButton, QRadioButton, QSlider, QSpinBox, QTimeEdit, QWidget)
from PySide6.QtCore import QSize, Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('widgets - QCheckBox')

        self.setFixedSize(QSize(400, 600))

        widget = QComboBox()
        widget.addItems(['jeden', 'dwa', 'trzy'])

        widget.currentIndexChanged.connect(self.indexChanged)
        widget.currentTextChanged.connect(self.textChanged)

        self.setCentralWidget(widget)

    def indexChanged(self, i):
        print(i)

    def textChanged(self, s):
        print(s)



app = QApplication()
window = MainWindow()
window.show()

app.exec()
