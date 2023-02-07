
from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QCheckBox, QComboBox, QDateEdit, QDateTimeEdit,
                               QDial, QDoubleSpinBox, QFontComboBox, QLabel, QLCDNumber, QLineEdit, QProgressBar,
                               QPushButton, QRadioButton, QSlider, QSpinBox, QTimeEdit, QWidget)
from PySide6.QtCore import QSize


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Events')

        self.setFixedSize(QSize(400, 600))

        layout = QVBoxLayout()
        widgets = [QCheckBox, QComboBox, QDateEdit, QDateTimeEdit, QDial, QDoubleSpinBox, QFontComboBox, QLabel,
                QLCDNumber, QLineEdit, QProgressBar, QPushButton, QRadioButton, QSlider, QSpinBox, QTimeEdit]

        for widget in widgets:
            layout.addWidget(widget())

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)


app = QApplication()
window = MainWindow()
window.show()

app.exec()
