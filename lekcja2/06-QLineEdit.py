from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QCheckBox, QComboBox, QDateEdit, QDateTimeEdit,
                               QDial, QDoubleSpinBox, QFontComboBox, QLabel, QLCDNumber, QLineEdit, QProgressBar,
                               QPushButton, QRadioButton, QSlider, QSpinBox, QTimeEdit, QWidget, QListWidget)
from PySide6.QtCore import QSize, Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('widgets - QlineEdit')

        self.setFixedSize(QSize(400, 600))

        widget = QLineEdit()
        widget.setMaxLength(10)
        widget.setPlaceholderText('Wpisz tu jakiś tekst')

        widget.returnPressed.connect(self.returnPressed)
        widget.selectionChanged.connect(self.selectionChanged)
        widget.textChanged.connect(self.textChanged)
        widget.textEdited.connect(self.textEdited)
        
        self.setCentralWidget(widget)

    def returnPressed(self):
        print('Wciśnięto')
        self.centralWidget().setText('OK!')

    def selectionChanged(self):
        print('Zmieniono zaznaczenie')
        self.centralWidget().selectedText()

    def textChanged(self, s):
        print('Zmieniono tekst')
        print(s)

    def textEdited(self, s):
        print('Zmieniono tekst')
        print(s)

app = QApplication()
window = MainWindow()
window.show()

app.exec()
