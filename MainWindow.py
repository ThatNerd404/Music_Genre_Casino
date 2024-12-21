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
"    background-image: url(C:/Users/MyCom/Desktop/.vscode/Github_Projects/Music_Genre_Casino/assests/Casino_BG_ROOM.png);\n"
"	background-repeat: no-repeat;\n"
"}\n"
"")
        self.Background_Widget = QWidget(MainWindow)
        self.Background_Widget.setObjectName(u"Background_Widget")
        self.Slot_Machine_Widget = QLabel(self.Background_Widget)
        self.Slot_Machine_Widget.setObjectName(u"Slot_Machine_Widget")
        self.Slot_Machine_Widget.setGeometry(QRect(520, 280, 311, 371))
        self.Slot_Machine_Widget.setPixmap(QPixmap(u"assests/Music_Genre_Slot_machine.png"))
        self.Slot_Machine_Widget.setScaledContents(True)
        self.Slot_Title_Widget = QLabel(self.Background_Widget)
        self.Slot_Title_Widget.setObjectName(u"Slot_Title_Widget")
        self.Slot_Title_Widget.setGeometry(QRect(220, 140, 111, 141))
        self.Slot_Title_Widget.setStyleSheet(u"color: black;\n"
"font-weight: bold;")
        self.Slot_Title_Widget.setTextFormat(Qt.AutoText)
        self.Slot_Title_Widget.setScaledContents(True)
        self.Slot_Title_Widget.setWordWrap(True)
        self.Slot_Result_Label = QLabel(self.Background_Widget)
        self.Slot_Result_Label.setObjectName(u"Slot_Result_Label")
        self.Slot_Result_Label.setGeometry(QRect(560, 380, 231, 91))
        self.Slot_Result_Label.setStyleSheet(u"color: black;\n"
"font-weight:bold;\n"
"text-align:center;")
        self.Slot_Result_Label.setAlignment(Qt.AlignCenter)
        self.Slot_Result_Label.setWordWrap(True)
        self.Slot_Lever_Widget = QPushButton(self.Background_Widget)
        self.Slot_Lever_Widget.setObjectName(u"Slot_Lever_Widget")
        self.Slot_Lever_Widget.setGeometry(QRect(810, 360, 141, 211))
        self.Slot_Lever_Widget.setAutoFillBackground(False)
        self.Slot_Lever_Widget.setStyleSheet(u"QPushButton {\n"
"    outline: none;  /* Removes the blue focus effect */\n"
"    border: none;   /* Removes any default border */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}\n"
"QPushButton:disabled {\n"
"    border:none;\n"
"    outline:none;\n"
"	qproperty-icon: url(:/assests\\Music_Genre_Casino_Lever.png);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"assests/Music_Genre_Casino_Lever.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Slot_Lever_Widget.setIcon(icon1)
        self.Slot_Lever_Widget.setIconSize(QSize(500, 400))
        self.Slot_Lever_Widget.setFlat(True)
        self.Speech_Bubble_widget = QLabel(self.Background_Widget)
        self.Speech_Bubble_widget.setObjectName(u"Speech_Bubble_widget")
        self.Speech_Bubble_widget.setGeometry(QRect(190, 120, 141, 181))
        self.Speech_Bubble_widget.setPixmap(QPixmap(u"assests/Speech Bubble.png"))
        self.Speech_Bubble_widget.setScaledContents(True)
        self.Dealer_Widget = QLabel(self.Background_Widget)
        self.Dealer_Widget.setObjectName(u"Dealer_Widget")
        self.Dealer_Widget.setGeometry(QRect(0, 250, 331, 431))
        self.Dealer_Widget.setMinimumSize(QSize(0, 0))
        self.Dealer_Widget.setMaximumSize(QSize(361, 551))
        self.Dealer_Widget.setPixmap(QPixmap(u"assests/Brayden_Pixel_Art.png"))
        self.Dealer_Widget.setScaledContents(True)
        self.label = QLabel(self.Background_Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(320, -60, 511, 391))
        self.label.setPixmap(QPixmap(u"assests/Casino_Sign.png"))
        self.label.setScaledContents(True)
        MainWindow.setCentralWidget(self.Background_Widget)
        self.Dealer_Widget.raise_()
        self.Slot_Machine_Widget.raise_()
        self.Slot_Result_Label.raise_()
        self.Slot_Lever_Widget.raise_()
        self.Speech_Bubble_widget.raise_()
        self.Slot_Title_Widget.raise_()
        self.label.raise_()

        self.retranslateUi(MainWindow)

        self.Slot_Lever_Widget.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Slot_Machine_Widget.setText("")
        self.Slot_Title_Widget.setText(QCoreApplication.translate("MainWindow", u"Pull the lever to generate a random music genre!", None))
        self.Slot_Result_Label.setText("")
        self.Speech_Bubble_widget.setText("")
        self.Dealer_Widget.setText("")
        self.label.setText("")
    # retranslateUi

