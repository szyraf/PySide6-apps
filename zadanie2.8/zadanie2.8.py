import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QTextEdit, QColorDialog, \
    QFontDialog
from PySide6.QtGui import QAction, QKeySequence, QTextCharFormat, QFont, QColor

# TODO: tworzenie nowego pliku, zapisywanie pliku, otwieranie istniejącego pliku
# TODO: formatowanie tekstu (pogrubienie, pochylenie, podkreślenie czcionki)
# TODO: wyrównywanie tekstu (do lewej, do środka, do prawej, justowanie)
# TODO: zmiana koloru i kroju czcionki.

font = QFont('Roboto', 24)
color = QColor(0, 0, 0)

class ColorFormatingWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Color Formating')
        self.resize(QSize(550, 350))

        finallayout = QVBoxLayout()

        self.colorPicker = QColorDialog()
        self.colorPicker.accepted.connect(self.colorChanged)
        self.colorPicker.rejected.connect(self.close)

        finallayout.addWidget(self.colorPicker)

        widget = QWidget()
        widget.setLayout(finallayout)
        self.setCentralWidget(widget)

    def colorChanged(self):
        global color
        color = self.colorPicker.selectedColor()
        self.close()

class FontFormatingWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Font Formating')
        self.resize(QSize(550, 350))

        finallayout = QVBoxLayout()

        self.fontPicker = QFontDialog()
        self.fontPicker.accepted.connect(self.fontChanged)
        self.fontPicker.rejected.connect(self.close)

        finallayout.addWidget(self.fontPicker)

        widget = QWidget()
        widget.setLayout(finallayout)
        self.setCentralWidget(widget)

    def fontChanged(self):
        global font
        font = self.fontPicker.selectedFont()
        self.close()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle('Notepad')
        self.resize(QSize(600, 350))

        finallayout = QVBoxLayout()

        self.textBox = QTextEdit()
        self.textBox.setFont(QFont('Roboto', 24))
        finallayout.addWidget(self.textBox)

        self.btn = QAction('&New', self)
        self.btn.triggered.connect(self.buttonClicked)
        self.btn.setShortcut(QKeySequence('Ctrl+N'))

        self.btn2 = QAction('&Open', self)
        self.btn2.triggered.connect(self.buttonClicked)
        self.btn2.setShortcut(QKeySequence('Ctrl+O'))

        self.btn3 = QAction('&Save', self)
        self.btn3.triggered.connect(self.buttonClicked)
        self.btn3.setShortcut(QKeySequence('Ctrl+S'))
        
        self.btn4 = QAction('&Bold', self)
        self.btn4.triggered.connect(self.buttonClicked)
        self.btn4.setShortcut(QKeySequence('Ctrl+B'))

        self.btn5 = QAction('&Italics', self)
        self.btn5.triggered.connect(self.buttonClicked)
        self.btn5.setShortcut(QKeySequence('Ctrl+I'))

        self.btn6 = QAction('&Underline', self)
        self.btn6.triggered.connect(self.buttonClicked)
        self.btn6.setShortcut(QKeySequence('Ctrl+U'))

        self.btn7 = QAction('&Left', self)
        self.btn7.triggered.connect(self.buttonClicked)

        self.btn8 = QAction('&Center', self)
        self.btn8.triggered.connect(self.buttonClicked)

        self.btn9 = QAction('&Right', self)
        self.btn9.triggered.connect(self.buttonClicked)

        self.btn10 = QAction('&Justify', self)
        self.btn10.triggered.connect(self.buttonClicked)

        self.btn11 = QAction('&Color', self)
        self.btn11.triggered.connect(self.buttonClicked)

        self.btn12 = QAction('&Font', self)
        self.btn12.triggered.connect(self.buttonClicked)

        menu = self.menuBar()

        fileMenu = menu.addMenu('&File')
        fileMenu.addAction(self.btn)
        fileMenu.addAction(self.btn2)
        fileMenu.addAction(self.btn3)

        editMenu = menu.addMenu('&Format')
        editMenu.addAction(self.btn4)
        editMenu.addAction(self.btn4)
        editMenu.addAction(self.btn5)
        editMenu.addAction(self.btn6)
        editMenu.addSeparator()
        editMenu.addAction(self.btn7)
        editMenu.addAction(self.btn8)
        editMenu.addAction(self.btn9)
        editMenu.addAction(self.btn10)
        editMenu.addSeparator()
        editMenu.addAction(self.btn11)
        editMenu.addAction(self.btn12)

        widget = QWidget()
        widget.setLayout(finallayout)
        self.setCentralWidget(widget)

        self.ColorFormatingWindow = ColorFormatingWindow()
        self.FontFormatingWindow = FontFormatingWindow()

    def buttonClicked(self):
        try:
            buttontext = self.sender().text()
            if buttontext == "&New":
                print("new")
            elif buttontext == "&Open":
                print("open")
            elif buttontext == "&Save":
                print("save")
            elif buttontext == "&Bold":
                self.textBox.setFontWeight(QFont.Bold if self.textBox.fontWeight() == QFont.Normal else QFont.Normal)
            elif buttontext == "&Italics":
                self.textBox.setFontItalic(not self.textBox.fontItalic())
            elif buttontext == "&Underline":
                self.textBox.setFontUnderline(not self.textBox.fontUnderline())
            elif buttontext == "&Left":
                self.textBox.setAlignment(Qt.AlignLeft)
            elif buttontext == "&Center":
                self.textBox.setAlignment(Qt.AlignCenter)
            elif buttontext == "&Right":
                self.textBox.setAlignment(Qt.AlignRight)
            elif buttontext == "&Justify":
                self.textBox.setAlignment(Qt.AlignJustify)
            elif buttontext == "&Color":
                self.ColorFormatingWindow.show()
            elif buttontext == "&Font":
                self.FontFormatingWindow.show()
            else:
                print("error")
        except:
            print('error')

    def closeEvent(self, event):
        self.ColorFormatingWindow.close()
        self.FontFormatingWindow.close()

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()