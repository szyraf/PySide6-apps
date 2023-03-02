# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)
import resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(345, 500)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 10, 321, 51))
        font = QFont()
        font.setPointSize(30)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 80, 322, 371))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pushButton_25 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_25.setObjectName(u"pushButton_25")
        icon = QIcon()
        icon.addFile(u":/icons/chart_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_25.setIcon(icon)

        self.horizontalLayout_8.addWidget(self.pushButton_25)

        self.pushButton_26 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_26.setObjectName(u"pushButton_26")

        self.horizontalLayout_8.addWidget(self.pushButton_26)

        self.pushButton_27 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_27.setObjectName(u"pushButton_27")

        self.horizontalLayout_8.addWidget(self.pushButton_27)

        self.pushButton_28 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_28.setObjectName(u"pushButton_28")

        self.horizontalLayout_8.addWidget(self.pushButton_28)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_21 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_21.setObjectName(u"pushButton_21")

        self.horizontalLayout_7.addWidget(self.pushButton_21)

        self.pushButton_22 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_22.setObjectName(u"pushButton_22")

        self.horizontalLayout_7.addWidget(self.pushButton_22)

        self.pushButton_23 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_23.setObjectName(u"pushButton_23")

        self.horizontalLayout_7.addWidget(self.pushButton_23)

        self.pushButton_24 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_24.setObjectName(u"pushButton_24")

        self.horizontalLayout_7.addWidget(self.pushButton_24)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton_17 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_17.setObjectName(u"pushButton_17")

        self.horizontalLayout_6.addWidget(self.pushButton_17)

        self.pushButton_18 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_18.setObjectName(u"pushButton_18")

        self.horizontalLayout_6.addWidget(self.pushButton_18)

        self.pushButton_19 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_19.setObjectName(u"pushButton_19")

        self.horizontalLayout_6.addWidget(self.pushButton_19)

        self.pushButton_20 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_20.setObjectName(u"pushButton_20")

        self.horizontalLayout_6.addWidget(self.pushButton_20)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_13 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.horizontalLayout_5.addWidget(self.pushButton_13)

        self.pushButton_14 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.horizontalLayout_5.addWidget(self.pushButton_14)

        self.pushButton_15 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_15.setObjectName(u"pushButton_15")

        self.horizontalLayout_5.addWidget(self.pushButton_15)

        self.pushButton_16 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_16.setObjectName(u"pushButton_16")

        self.horizontalLayout_5.addWidget(self.pushButton_16)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_9 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.horizontalLayout_4.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.horizontalLayout_4.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.horizontalLayout_4.addWidget(self.pushButton_11)

        self.pushButton_12 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.horizontalLayout_4.addWidget(self.pushButton_12)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_5 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_3.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout_3.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout_3.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.horizontalLayout_3.addWidget(self.pushButton_8)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout.addWidget(self.pushButton_4)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 345, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"wykresy", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"CE", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"\u232b", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"1/x", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"x\u00b2", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"\u221ax", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"\u00f7", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u",", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"sin", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"cos", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"tg", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"ctg", None))
    # retranslateUi

