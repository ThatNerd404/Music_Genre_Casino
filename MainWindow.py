# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 675)
        MainWindow.setMinimumSize(QSize(1200, 675))
        MainWindow.setMaximumSize(QSize(1200, 675))
        icon = QIcon()
        icon.addFile(u"assests/icons8-slot-machine-48.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"#Background_Widget {\n"
"    background-image: url(C:/Users/MyCom/Desktop/.vscode/Github_Projects/Music_Genre_Casino/assests/Casino_BG_tiny.png);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}")
        self.Background_Widget = QWidget(MainWindow)
        self.Background_Widget.setObjectName(u"Background_Widget")
        self.Slot_Machine_Widget = QLabel(self.Background_Widget)
        self.Slot_Machine_Widget.setObjectName(u"Slot_Machine_Widget")
        self.Slot_Machine_Widget.setGeometry(QRect(600, 70, 421, 581))
        self.Slot_Machine_Widget.setPixmap(QPixmap(u"assests/Slot_Machine.png"))
        self.Slot_Machine_Widget.setScaledContents(True)
        self.Slot_Title_Widget = QLabel(self.Background_Widget)
        self.Slot_Title_Widget.setObjectName(u"Slot_Title_Widget")
        self.Slot_Title_Widget.setGeometry(QRect(670, 150, 281, 16))
        self.Slot_Title_Widget.setStyleSheet(u"color: black")
        self.Slot_Result_Label = QLabel(self.Background_Widget)
        self.Slot_Result_Label.setObjectName(u"Slot_Result_Label")
        self.Slot_Result_Label.setGeometry(QRect(680, 260, 251, 51))
        self.Slot_Result_Label.setStyleSheet(u"color: black")
        self.Slot_Lever_Widget = QPushButton(self.Background_Widget)
        self.Slot_Lever_Widget.setObjectName(u"Slot_Lever_Widget")
        self.Slot_Lever_Widget.setGeometry(QRect(950, 250, 151, 241))
        self.Slot_Lever_Widget.setAutoFillBackground(False)
        self.Slot_Lever_Widget.setStyleSheet(u"QPushButton {\n"
"    outline: none;  /* Removes the blue focus effect */\n"
"    border: none;   /* Removes any default border */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"assests/Slot_Machine_Lever.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Slot_Lever_Widget.setIcon(icon1)
        self.Slot_Lever_Widget.setIconSize(QSize(100, 600))
        self.Slot_Lever_Widget.setFlat(True)
        MainWindow.setCentralWidget(self.Background_Widget)

        self.retranslateUi(MainWindow)

        self.Slot_Lever_Widget.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Slot_Machine_Widget.setText("")
        self.Slot_Title_Widget.setText(QCoreApplication.translate("MainWindow", u" Pull the lever to generate a random music genre!", None))
        self.Slot_Result_Label.setText("")
    # retranslateUi

