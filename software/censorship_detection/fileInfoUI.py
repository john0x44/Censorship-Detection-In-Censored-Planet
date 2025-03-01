# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'file_infoqKlCZd.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class FileInfoUI(object):    
    def setupUi(self, MainWindow):
        self.FileMetaData = None
        self.MainWindow = MainWindow

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"FileInfo")
        MainWindow.resize(800, 416)
        MainWindow.setStyleSheet(u"background-color: black;\n"
"color: white;\n"
"Border: 0.5px solid white;\n"
"\n"
"          ")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{Border:0px}\n"
"QScrollBar:sub-page:vertical{background-color: #000000}\n"
"QScrollBar:add-page:vertical{background-color: #000000}\n"
"QScrollBar{background-color: #000000}\n"
"QScrollBar:sub-page:vertical{background-color: #000000} QScrollBar:add-page:vertical{background-color: #000000} QScrollBar{background-color: #000000}\n"
"QScrollBar::add-line:vertical { background-color: transparent}\n"
"QScrollBar::sub-line:vertical { background-color: transparent}\n"
"QScrollBar::handle:vertical {background-color: rgba(80, 80, 122, .25);}\n"
"QPushButton{color: gray}\n"
"QPushButton:hover{color: white}\n"
"\n"
"QScrollBar:sub-page:horizontal{background-color: #000000}\n"
"QScrollBar:add-page:horizontal{background-color: #000000}\n"
"QScrollBar{background-color: #000000}\n"
"QScrollBar:sub-page:horizontal{background-color: #000000} QScrollBar:add-page:horizontal{background-color: #000000} QScrollBar{background-color: #000000}\n"
"QScrollBar::add-line:horizontal { background-color: transparent}\n"
"QScrollBar::sub-li"
                        "ne:horizontal { background-color: transparent}\n"
"QScrollBar::handle:horizontal{background-color: rgba(80, 80, 122, .2);}\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"Border-Bottom: 3px solid rgba(255,255,255,0.05);\n"
"")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.label_6.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_6)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"Border-Bottom: 3px solid rgba(255,255,255,0.025);\n"
"")

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"Border-Bottom: 3px solid rgba(255,255,255,0.025);\n"
"")

        self.verticalLayout_2.addWidget(self.label_4)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"Border-Bottom: 3px solid rgba(255,255,255,0.025);\n"
"")

        self.verticalLayout_2.addWidget(self.label_3)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.label_5)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def updateFileMetaDataUI(self):
        self.label.setText(f"DETAIL ABOUT FILE [{self.FileMetaData['FileName']}]")
        self.label_6.setText(f"FROM DATASET | [{self.FileMetaData['DirectoryFrom']}]")
        self.label_2.setText(f"FILE NAME | [{self.FileMetaData['FileName']}]")
        self.label_4.setText(f"FILE SIZE | [{self.FileMetaData['MBSize']}][MB]")
        self.label_3.setText(f"COUNTRY | [{self.FileMetaData['Country']}]")
        self.label_5.setText(f"DATE | [{self.FileMetaData['FileDate']}]")

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("FileInfo")
        self.label.setText(QCoreApplication.translate("MainWindow", u"DETAILS ABOUT FILE ", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"FROM DATASET | ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"FILE NAME | ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"FILE SIZE | ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"COUNTRY | ", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"DATE | ", None))
    # retranslateUi
