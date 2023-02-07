from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QMenu
from PySide6.QtCore import QSize
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Events')

        self.setMinimumSize(QSize(300, 300))
        self.setMaximumSize(QSize(500, 500))

    def contextMenuEvent(self, e):
        context = QMenu(self)
        context.addAction(QAction('Test 1', self))
        context.addAction(QAction('Test 2', self))
        context.addAction(QAction('Test 3', self))
        context.exec(e.globalPos())


app = QApplication()
window = MainWindow()
window.show()

app.exec()
