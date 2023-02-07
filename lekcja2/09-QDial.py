# QDial
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QDial

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QDial")

        widget = QDial()
        widget.setRange(-10, 100)
        widget.setSingleStep(0.5)

        widget.valueChanged.connect(self.valueChanged)
        widget.sliderMoved.connect(self.sliderPosition)
        widget.sliderPressed.connect(self.sliderPressed)
        widget.sliderReleased.connect(self.sliderReleased)

        self.setCentralWidget(widget)

    def valueChanged(self, i):
        print(i)

    def sliderPosition(self, p):
        print("position", p)

    def sliderPressed(self):
        print("Pressed!")

    def sliderReleased(self):
        print("Released")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
