from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QCheckBox, QComboBox, QDateEdit, QDateTimeEdit,
                               QDial, QDoubleSpinBox, QFontComboBox, QLabel, QLCDNumber, QLineEdit, QProgressBar,
                               QPushButton, QRadioButton, QSlider, QSpinBox, QTimeEdit, QWidget, QListWidget)
from PySide6.QtCore import QSize, Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Zadanie1.1')

        self.setFixedSize(QSize(400, 600))

        layout = QVBoxLayout()

        self.lineEdit = QLineEdit()
        self.lineEdit.setPlaceholderText('Wpisz liczby oddzielone przecinkiem')
        layout.addWidget(self.lineEdit)

        self.button = QPushButton('Policz')
        self.button.setCheckable(True)
        self.button.clicked.connect(self.buttonClicked)
        layout.addWidget(self.button)

        self.label = QLabel('1')
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def buttonClicked(self):
        inputText = self.lineEdit.text().replace(" ", "").split(",")

        inputText2 = []

        suma = 0
        for number in inputText:
            suma += int(number)
            inputText2.append(int(number))

        inputText2.sort(reverse=True)

        inputText3 = []
        for a in inputText2:
            inputText3.append(str(a))

        string = ",".join(inputText3) + "\nmin: " + inputText3[len(inputText3) - 1] + "\nmax: " + inputText3[0]

        string += "\nŚrednia: " + str(suma / len(inputText3))

        self.label.setText(string)

app = QApplication()
window = MainWindow()
window.show()

app.exec()
