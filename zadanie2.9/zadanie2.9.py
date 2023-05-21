import sys

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

primaryColor = QColor(0, 0, 0)
secondaryColor = QColor(255, 255, 255)
whichColor = 0
whichTool = 0
history = []
historyPosition = -1
canvasSelf = None
MainWindowSelf = None


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
        global primaryColor
        global secondaryColor
        global whichColor
        
        if whichColor == 0:
            primaryColor = self.colorPicker.selectedColor()
        else:
            secondaryColor = self.colorPicker.selectedColor()
        self.close()

class Canvas(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()

        pixmap = QtGui.QPixmap(800, 450)
        pixmap.fill(Qt.white)
        self.setPixmap(pixmap)

        global canvasSelf
        canvasSelf = self

        self.last_x, self.last_y = None, None
        self.start_x, self.start_y = None, None

    def mousePressEvent(self, e):
        mousePosition = e.position().toPoint()
        canvas = self.pixmap()
        painter = QtGui.QPainter(canvas)
        pen = painter.pen()

        global whichTool
        global primaryColor
        global secondaryColor

        if whichTool == 0:
            pen.setWidth(4)
            if e.buttons() & QtCore.Qt.LeftButton:
                pen.setColor(primaryColor)
            elif e.buttons() & QtCore.Qt.RightButton:
                pen.setColor(secondaryColor)

            painter.setPen(pen)
            painter.drawPoint(mousePosition.x(), mousePosition.y())
            painter.end()
            self.setPixmap(canvas)

            self.last_x = mousePosition.x()
            self.last_y = mousePosition.y()
        elif whichTool == 1:
            pen.setWidth(30)
            if e.buttons() & QtCore.Qt.LeftButton:
                pen.setColor(secondaryColor)
            if e.buttons() & QtCore.Qt.RightButton:
                painter.end()
                return
            painter.setPen(pen)
            painter.drawPoint(mousePosition.x(), mousePosition.y())
            painter.end()
            self.setPixmap(canvas)
        elif whichTool == 2 or whichTool == 3 or whichTool == 4:
            painter.end()
            self.start_x = mousePosition.x()
            self.start_y = mousePosition.y()  


    def mouseMoveEvent(self, e):
        mousePosition = e.position().toPoint()
        canvas = self.pixmap()
        painter = QtGui.QPainter(canvas)
        pen = painter.pen()
        
        global whichTool
        global primaryColor
        global secondaryColor
        global history
        global historyPosition
        global canvasSelf

        if whichTool == 0:
            pen.setWidth(4)

            if e.buttons() & QtCore.Qt.LeftButton:
                pen.setColor(primaryColor)
            elif e.buttons() & QtCore.Qt.RightButton:
                pen.setColor(secondaryColor)
            
            painter.setPen(pen)
            if self.last_x is not None and self.last_y is not None:
                painter.drawLine(self.last_x, self.last_y, mousePosition.x(), mousePosition.y())
            painter.end()
            self.setPixmap(canvas)

            self.last_x = mousePosition.x()
            self.last_y = mousePosition.y()
        elif whichTool == 1:
            pen.setWidth(30)

            if e.buttons() & QtCore.Qt.LeftButton:
                pen.setColor(secondaryColor)
            if e.buttons() & QtCore.Qt.RightButton:
                painter.end()
                return
            
            painter.setPen(pen)
            if self.last_x is not None and self.last_y is not None:
                painter.drawLine(self.last_x, self.last_y, mousePosition.x(), mousePosition.y())
            painter.end()
            self.setPixmap(canvas)

            self.last_x = mousePosition.x()
            self.last_y = mousePosition.y()
        elif whichTool == 2 or whichTool == 3 or whichTool == 4:
            painter.end()
            if historyPosition > -1:
                self.setPixmap(history[historyPosition])
            else:
                pixmap = QtGui.QPixmap(800, 450)
                pixmap.fill(Qt.white)
                self.setPixmap(pixmap)

            canvas = self.pixmap()
            painter = QtGui.QPainter(canvas)
            pen = painter.pen()

            pen.setWidth(4)

            brushColor = 0

            if e.buttons() & QtCore.Qt.LeftButton:
                pen.setColor(primaryColor)
                brushColor = 1
            elif e.buttons() & QtCore.Qt.RightButton:
                pen.setColor(secondaryColor)
            
            painter.setPen(pen)
            if self.start_x is not None and self.start_y is not None:
                if whichTool == 2:
                    painter.drawLine(self.start_x, self.start_y, mousePosition.x(), mousePosition.y())
                elif whichTool == 3:
                    if brushColor == 0:
                        painter.setBrush(QtGui.QBrush(primaryColor))
                    else:
                        painter.setBrush(QtGui.QBrush(secondaryColor))
                    if e.modifiers() & QtCore.Qt.ShiftModifier:
                        if (abs(mousePosition.x() - self.start_x)) > (abs(mousePosition.y() - self.start_y)):
                            size = abs(mousePosition.x() - self.start_x)
                            painter.drawRect(self.start_x, self.start_y, size * (1 if mousePosition.x() > self.start_x else -1), size * (1 if mousePosition.y() > self.start_y else -1))
                        else:
                            size = abs(mousePosition.y() - self.start_y)
                            painter.drawRect(self.start_x, self.start_y, size * (1 if mousePosition.x() > self.start_x else -1), size * (1 if mousePosition.y() > self.start_y else -1))  
                    else:
                        painter.drawRect(self.start_x, self.start_y, mousePosition.x() - self.start_x, mousePosition.y() - self.start_y)
                elif whichTool == 4:
                    if brushColor == 0:
                        painter.setBrush(QtGui.QBrush(primaryColor))
                    else:
                        painter.setBrush(QtGui.QBrush(secondaryColor))
                    if e.modifiers() & QtCore.Qt.ShiftModifier:
                        if (abs(mousePosition.x() - self.start_x)) > (abs(mousePosition.y() - self.start_y)):
                            size = abs(mousePosition.x() - self.start_x)
                            painter.drawEllipse(self.start_x, self.start_y, size * (1 if mousePosition.x() > self.start_x else -1), size * (1 if mousePosition.y() > self.start_y else -1))
                        else:
                            size = abs(mousePosition.y() - self.start_y)
                            painter.drawEllipse(self.start_x, self.start_y, size * (1 if mousePosition.x() > self.start_x else -1), size * (1 if mousePosition.y() > self.start_y else -1))
                    else:
                        painter.drawEllipse(self.start_x, self.start_y, mousePosition.x() - self.start_x, mousePosition.y() - self.start_y)

            painter.end()
            self.setPixmap(canvas)
            

    def mouseReleaseEvent(self, e):
        self.last_x = None
        self.last_y = None

        global history
        global historyPosition
        historyPosition += 1
        history = history[:historyPosition]
        history.append(self.pixmap().copy())
    
    def increase_filter(self, pixmap, r, g, b):
        image = pixmap.toImage()  # Convert the QPixmap to QImage
        width = image.width()
        height = image.height()

        for y in range(height):
            for x in range(width):
                pixel = image.pixelColor(x, y)
                red = min(max(pixel.red() + r, 0), 255)
                green = min(max(pixel.green() + g, 0), 255)
                blue = min(max(pixel.blue() + b, 0), 255)
                image.setPixelColor(x, y, QColor(red, green, blue))

        global history
        global historyPosition

        historyPosition += 1
        history = history[:historyPosition]
        history.append(QPixmap.fromImage(image))

        return QPixmap.fromImage(image)  # Convert the QImage back to QPixmap

class QPaletteButton(QtWidgets.QPushButton):
    def __init__(self, color):
        super().__init__()
        self.setFixedSize(QtCore.QSize(24, 24))
        self.color = color
        self.setStyleSheet("background-color: %s;" % color)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Paint')
        self.resize(QSize(800, 450))

        global MainWindowSelf
        MainWindowSelf = self

        finallayout = QtWidgets.QVBoxLayout()
        self.widget = QtWidgets.QWidget()

        finallayout.setAlignment(Qt.AlignTop)
        
        self.canvas = Canvas()
        finallayout.addWidget(self.canvas)

        self.palette = QtWidgets.QHBoxLayout()
        finallayout.addLayout(self.palette)

        self.btn = QAction('&New', self)
        self.btn.triggered.connect(self.buttonClicked)
        self.btn.setShortcut(QKeySequence('Ctrl+N'))

        self.btn2 = QAction('&Open', self)
        self.btn2.triggered.connect(self.buttonClicked)
        self.btn2.setShortcut(QKeySequence('Ctrl+O'))

        self.btn3 = QAction('&Save', self)
        self.btn3.triggered.connect(self.buttonClicked)
        self.btn3.setShortcut(QKeySequence('Ctrl+S'))

        self.btn4 = QAction('&Undo', self)
        self.btn4.triggered.connect(self.buttonClicked)
        self.btn4.setShortcut(QKeySequence('Ctrl+Z'))

        self.btn5 = QAction('&Redo', self)
        self.btn5.triggered.connect(self.buttonClicked)
        self.btn5.setShortcut(QKeySequence('Ctrl+Y'))

        self.btn6 = QAction('&Primary Color', self)
        self.btn6.triggered.connect(self.buttonClicked)

        self.btn7 = QAction('&Secondary Color', self)
        self.btn7.triggered.connect(self.buttonClicked)

        self.btn8 = QAction('&Pen', self)
        self.btn8.triggered.connect(self.buttonClicked)

        self.btn9 = QAction('&Eraser', self)
        self.btn9.triggered.connect(self.buttonClicked)

        self.btn10 = QAction('&Line', self)
        self.btn10.triggered.connect(self.buttonClicked)

        self.btn11 = QAction('&Rectangle', self)
        self.btn11.triggered.connect(self.buttonClicked)

        self.btn12 = QAction('&Circle', self)
        self.btn12.triggered.connect(self.buttonClicked)

        self.btn13 = QAction('&More Red', self)
        self.btn13.triggered.connect(self.buttonClicked)

        self.btn14 = QAction('&More Green', self)
        self.btn14.triggered.connect(self.buttonClicked)

        self.btn15 = QAction('&More Blue', self)
        self.btn15.triggered.connect(self.buttonClicked)

        menu = self.menuBar()

        fileMenu = menu.addMenu('&File')
        fileMenu.addAction(self.btn)
        fileMenu.addAction(self.btn2)
        fileMenu.addAction(self.btn3)

        editMenu = menu.addMenu('&Edit')
        editMenu.addAction(self.btn4)
        editMenu.addAction(self.btn5)

        colorMenu = menu.addMenu('&Colors')
        colorMenu.addAction(self.btn6)
        colorMenu.addAction(self.btn7)

        toolMenu = menu.addMenu('&Tools')
        toolMenu.addAction(self.btn8)
        toolMenu.addAction(self.btn9)
        toolMenu.addAction(self.btn10)
        toolMenu.addAction(self.btn11)
        toolMenu.addAction(self.btn12)

        filterMenu = menu.addMenu('&Filters')
        filterMenu.addAction(self.btn13)
        filterMenu.addAction(self.btn14)
        filterMenu.addAction(self.btn15)

        self.widget.setLayout(finallayout)
        self.setCentralWidget(self.widget)
        

    def buttonClicked(self):
        global history
        global historyPosition
        global whichTool

        try:
            buttontext = self.sender().text()
            if buttontext == "&New":
                history = []
                historyPosition = -1
                
                pixmap = QtGui.QPixmap(800, 450)
                pixmap.fill(Qt.white)
                canvasSelf.setPixmap(pixmap)
            elif buttontext == "&Open":
                filename, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*)')

                if filename == "":
                    return
                
                pixmap = QtGui.QPixmap(filename)
                canvasSelf.setPixmap(pixmap)

                history = []
                history.append(pixmap.copy())
                historyPosition = 0
            elif buttontext == "&Save":
                filename, _ = QFileDialog.getSaveFileName(self, 'Save File', '', 'PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*)')
                
                if filename == "":
                    return

                pixmap = self.canvas.pixmap()
                pixmap.save(filename, 'png')                
            elif buttontext == "&Undo":
                if len(history) > 0:
                    historyPosition -= 1
                    if historyPosition > -1:
                        canvasSelf.setPixmap(history[historyPosition])
                    else:
                        historyPosition = -1
                        pixmap = QtGui.QPixmap(800, 450)
                        pixmap.fill(Qt.white)
                        canvasSelf.setPixmap(pixmap)
            elif buttontext == "&Redo":
                if len(history) > 0:
                    historyPosition += 1
                    if historyPosition < len(history):
                        canvasSelf.setPixmap(history[historyPosition])
                    else:
                        historyPosition -= 1
            elif buttontext == "&Primary Color":
                self.set_primary_color()
            elif buttontext == "&Secondary Color":
                self.set_secondary_color()
            elif buttontext == "&Pen":
                whichTool = 0
            elif buttontext == "&Eraser":
                whichTool = 1
            elif buttontext == "&Line":
                whichTool = 2
            elif buttontext == "&Rectangle":
                whichTool = 3
            elif buttontext == "&Circle":
                whichTool = 4
            elif buttontext == "&More Red":
                canvasSelf.setPixmap(canvasSelf.increase_filter(canvasSelf.pixmap().copy(), 60, -60, -60))
            elif buttontext == "&More Green":
                canvasSelf.setPixmap(canvasSelf.increase_filter(canvasSelf.pixmap().copy(), -60, 60, -60))
            elif buttontext == "&More Blue":
                canvasSelf.setPixmap(canvasSelf.increase_filter(canvasSelf.pixmap().copy(), -60, -60, 60))
        except:
            print('error')

    def set_primary_color(self):
        global whichColor
        whichColor = 0
        self.ColorFormatingWindow = ColorFormatingWindow()
        self.ColorFormatingWindow.show()

    def set_secondary_color(self):
        global whichColor
        whichColor = 1
        self.ColorFormatingWindow = ColorFormatingWindow()
        self.ColorFormatingWindow.show()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
