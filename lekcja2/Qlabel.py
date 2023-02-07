from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QCheckBox, QComboBox, QDateEdit, QDateTimeEdit,
                               QDial, QDoubleSpinBox, QFontComboBox, QLabel, QLCDNumber, QLineEdit, QProgressBar,
                               QPushButton, QRadioButton, QSlider, QSpinBox, QTimeEdit, QWidget)
from PySide6.QtCore import QSize, Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('widgets - QLabel')

        self.setFixedSize(QSize(400, 600))

        widget = QLabel('Hello')
        font = widget.font()
        font.setPointSize(30)
        widget.setFont(font)

        # widget.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        widget.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(widget)


app = QApplication()
window = MainWindow()
window.show()

app.exec()
