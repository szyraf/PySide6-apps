from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QCheckBox, QComboBox, QDateEdit, QDateTimeEdit,
                               QDial, QDoubleSpinBox, QFontComboBox, QLabel, QLCDNumber, QLineEdit, QProgressBar,
                               QPushButton, QRadioButton, QSlider, QSpinBox, QTimeEdit, QWidget, QListWidget)
from PySide6.QtCore import QSize, Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('widgets - QSpinBox')

        self.setFixedSize(QSize(400, 600))

        widget = QSpinBox()

        widget.setMinimum(-10)
        widget.setMaximum(3)

        widget.setPrefix('$')
        widget.setSuffix('c')
        widget.setSingleStep(3)

        widget.valueChanged.connect(self.valueChanged)
        widget.textChanged.connect(self.valueChangedStr)

        self.setCentralWidget(widget)

    def valueChanged(self, i):
        print(i)

    def valueChangedStr(self, s):
        print(s)

    def textEdited(self, s):
        print('Edycja tekstu')
        print(s)

app = QApplication()
window = MainWindow()
window.show()

app.exec()
