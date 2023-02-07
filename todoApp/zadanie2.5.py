import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import sqlite3
import datetime

connection = sqlite3.connect('tasks.db')
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT,
    date TEXT,
    time TEXT,
    status TEXT
)""")
connection.commit()

last_task = []

class SetTimeAndDateWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setWindowTitle('Set time and date')
        self.setFixedSize(QSize(300, 200))

        self.date = QDateEdit()
        self.date.setDisplayFormat("dd.MM.yyyy")
        self.date.setCalendarPopup(True)
        layout.addWidget(self.date)

        self.time = QTimeEdit()
        self.time.setDisplayFormat("hh:mm")
        layout.addWidget(self.time)

        self.button = QPushButton("Save")
        self.button.clicked.connect(self.save)
        layout.addWidget(self.button)
        
        self.setLayout(layout)

    def updateTime(self):
        self.date.setDate(QDate.fromString(last_task[2], "dd.MM.yyyy"))
        self.time.setTime(QTime.fromString(last_task[3], "hh:mm"))
    
    def save(self):
        date = self.date.date().toString("dd.MM.yyyy")
        time = self.time.time().toString("hh:mm")
        
        cursor.execute("UPDATE tasks SET date = ?, time = ? WHERE id = ?", (date, time, last_task[0]))
        connection.commit()

        window.updateTasks()

        self.close()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window = SetTimeAndDateWindow()

        self.tasks = []

        self.setWindowTitle('Zadanie2.5')
        self.setFixedSize(QSize(600, 400))

        finallayout = QVBoxLayout()

        self.listWidget = QListWidget()
        self.listWidget.setFixedHeight(350)
        self.listWidget.setStyleSheet("QListWidget { font-size: 30px }")
        
        self.updateTasks()

        finallayout.addWidget(self.listWidget)

        self.btn = QAction('&Add task', self)
        self.btn.triggered.connect(self.buttonClicked)
        self.btn.setShortcut(QKeySequence('Ctrl+1'))

        self.btn2 = QAction('&Edit task', self)
        self.btn2.triggered.connect(self.buttonClicked)
        self.btn2.setShortcut(QKeySequence('Ctrl+2'))

        self.btn3 = QAction('&Delete task', self)
        self.btn3.triggered.connect(self.buttonClicked)
        self.btn3.setShortcut(QKeySequence('Ctrl+3'))

        self.btn4 = QAction('&Mark as done', self)
        self.btn4.triggered.connect(self.buttonClicked)
        self.btn4.setShortcut(QKeySequence('Ctrl+4'))

        self.btn5 = QAction('&Mark as undone', self)
        self.btn5.triggered.connect(self.buttonClicked)
        self.btn5.setShortcut(QKeySequence('Ctrl+5'))

        self.btn6 = QAction('&Set date and time', self)
        self.btn6.triggered.connect(self.buttonClicked)
        self.btn6.setShortcut(QKeySequence('Ctrl+6'))

        self.toolbar = self.addToolBar('Toolbar')
        self.toolbar.addAction(self.btn)
        self.toolbar.addAction(self.btn2)
        self.toolbar.addAction(self.btn3)
        self.toolbar.addAction(self.btn4)
        self.toolbar.addAction(self.btn5)
        self.toolbar.addAction(self.btn6)

        widget = QWidget()
        widget.setLayout(finallayout)
        self.setCentralWidget(widget)

    def updateTasks(self):
        cursor.execute("SELECT * FROM tasks")
        self.tasks = cursor.fetchall()
        self.listWidget.clear()
        for task in self.tasks:
            self.listWidget.addItem(task[1])
            if len(task) == 5:
                if task[2] != None and task[3] != None:
                    label = QLabel(task[2] + ' ' + task[3])
                    label.setStyleSheet("QLabel { font-size: 18px }")
                    label.setAlignment(Qt.AlignRight)
                    if datetime.datetime.strptime(task[2], "%d.%m.%Y").date() < datetime.date.today() or datetime.datetime.strptime(task[3], "%H:%M").time() < datetime.datetime.now().time():
                        label.setStyleSheet("QLabel { font-size: 18px; color: red }")
                    self.listWidget.setItemWidget(self.listWidget.item(self.listWidget.count() - 1), label)

                if task[4] == 'Done':
                    font = self.listWidget.item(self.listWidget.count() - 1).font()
                    font.setStrikeOut(True)
                    self.listWidget.item(self.listWidget.count() - 1).setFont(font)
                elif task[4] == 'Not done':
                    font = self.listWidget.item(self.listWidget.count() - 1).font()
                    font.setStrikeOut(False)
                    self.listWidget.item(self.listWidget.count() - 1).setFont(font)

    def buttonClicked(self):
        sender = self.sender()
        if sender.text() == '&Add task':
            self.addTask()
        elif sender.text() == '&Edit task':
            self.editTask()
        elif sender.text() == '&Delete task':
            self.deleteTask()
        elif sender.text() == '&Mark as done':
            self.markAsDone()
        elif sender.text() == '&Mark as undone':
            self.markAsUndone()
        elif sender.text() == '&Set date and time':
            self.setDateTime()
    
    def addTask(self):
        text, ok = QInputDialog.getText(self, 'Add task', 'Enter task name:')
        if ok and text != '':
            cursor.execute("INSERT INTO tasks (task, date, time, status) VALUES (?, ?, ?, ?)", (text, datetime.date.today().strftime('%d.%m.%Y'), datetime.datetime.now().strftime('%H:%M'), 'Not done'))
            connection.commit()
            self.updateTasks()
    
    def editTask(self):
        if self.listWidget.currentItem() is not None:
            text, ok = QInputDialog.getText(self, 'Edit task', 'Enter task name:')
            if ok and text != '':
                cursor.execute("UPDATE tasks SET task = ? WHERE id = ?", (text, self.tasks[self.listWidget.currentRow()][0]))
                connection.commit()
                self.updateTasks()
    
    def deleteTask(self):
        if self.listWidget.currentItem() is not None:
            cursor.execute("DELETE FROM tasks WHERE id = ?", (self.tasks[self.listWidget.currentRow()][0],))
            connection.commit()
            self.updateTasks()
    
    def markAsDone(self):
        if self.listWidget.currentItem() is not None:
            cursor.execute("UPDATE tasks SET status = ? WHERE id = ?", ('Done', self.tasks[self.listWidget.currentRow()][0]))
            connection.commit()

            font = self.listWidget.currentItem().font()
            font.setStrikeOut(True)
            self.listWidget.currentItem().setFont(font)

    def markAsUndone(self):
        if self.listWidget.currentItem() is not None:
            cursor.execute("UPDATE tasks SET status = ? WHERE id = ?", ('Not done', self.tasks[self.listWidget.currentRow()][0]))
            connection.commit()
            
            font = self.listWidget.currentItem().font()
            font.setStrikeOut(False)
            self.listWidget.currentItem().setFont(font)

    def setDateTime(self):
        if self.listWidget.currentItem() is not None:
            if self.window.isVisible():
                self.window.hide()
            else:
                global last_task
                last_task = self.tasks[self.listWidget.currentRow()]
                self.window.updateTime()
                self.window.show()

    def setTime(self, time):
        self.listWidget.currentItem().setText(time.toString())

    def setDate(self, date):
        self.listWidget.currentItem().setText(date.toString())

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', 'Are you sure to quit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()