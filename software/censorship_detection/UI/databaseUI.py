# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'databasebgjtKR.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class DatabaseUI(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"Database")
        MainWindow.resize(1230, 625)
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
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 35))
        self.frame_2.setStyleSheet(u"Border-Bottom: 3px solid rgba(255,255,255,0.05);\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMaximumSize(QSize(35, 16777215))
        icon = QIcon()
        icon.addFile(u"icons/database.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(23, 23))

        self.horizontalLayout.addWidget(self.pushButton)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.pushButton_7 = QPushButton(self.frame_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setMaximumSize(QSize(150, 16777215))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        self.pushButton_7.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(u"icons/clock.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon1)
        self.pushButton_7.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.frame_2)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setMaximumSize(QSize(180, 16777215))
        self.pushButton_8.setFont(font1)
        self.pushButton_8.setStyleSheet(u"Border-Right: 3px solid rgba(255,255,255,0.05);")
        icon2 = QIcon()
        icon2.addFile(u"icons/web.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon2)

        self.horizontalLayout.addWidget(self.pushButton_8)
        

        self.pushButton_9 = QPushButton(self.frame_2)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setMaximumSize(QSize(190, 16777215))
        self.pushButton_9.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(u"icons/country.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon3)
        self.pushButton_9.setIconSize(QSize(22, 22))

        self.horizontalLayout.addWidget(self.pushButton_9)
        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"Border-Right: 3px solid rgba(255,255,255,0.05);\n"
"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 35))
        self.frame_7.setStyleSheet(u"Border-Right: 0px;\n"
"Border-Bottom: 3px solid rgba(255,255,255,0.02);\n"
"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.frame_7)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMaximumSize(QSize(40, 16777215))
        icon2 = QIcon()
        icon2.addFile(u"icons/anomaly.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.label_2 = QLabel(self.frame_7)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(180,180,180);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_2)


        self.verticalLayout_3.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_4)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"Border-Right: 0px;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_8)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.frame_8)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 401, 439))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 35))

        self.verticalLayout_9.addWidget(self.label_5, 0, Qt.AlignTop)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_6.addWidget(self.scrollArea)


        self.verticalLayout_3.addWidget(self.frame_8)


        self.horizontalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"Border-Right: 3px solid rgba(255,255,255,0.05);\n"
"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_5)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(16777215, 35))
        self.frame_9.setStyleSheet(u"Border-Right: 0px;\n"
"Border-Bottom: 3px solid rgba(255,255,255,0.02);\n"
"")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.frame_9)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMaximumSize(QSize(40, 16777215))
        icon3 = QIcon()
        icon3.addFile(u"icons/country.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setIconSize(QSize(25, 25))

        self.horizontalLayout_4.addWidget(self.pushButton_3)

        self.label_3 = QLabel(self.frame_9)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: rgb(180,180,180);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_3)


        self.verticalLayout_4.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_5)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"Border-Right: 0px;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_10)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.frame_10)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        sizePolicy.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 401, 439))
        self.verticalLayout_10 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_6 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 35))
        self.label_6.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_10.addWidget(self.label_6, 0, Qt.AlignTop)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_7.addWidget(self.scrollArea_2)


        self.verticalLayout_4.addWidget(self.frame_10)


        self.horizontalLayout_2.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"Border-Right: 0px;\n"
"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.frame_6)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(16777215, 35))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(False)
        font2.setWeight(50)
        self.frame_11.setFont(font2)
        self.frame_11.setStyleSheet(u"Border-Right: 0px;\n"
"Border-Bottom: 3px solid rgba(255,255,255,0.02);\n"
"")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.frame_11)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMaximumSize(QSize(40, 16777215))
        icon4 = QIcon()
        icon4.addFile(u"icons/blocked.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon4)
        self.pushButton_4.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.pushButton_4)

        self.label_4 = QLabel(self.frame_11)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: rgb(180,180,180);")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_4)


        self.verticalLayout_5.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_6)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"Border-Right: 0px;")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_12)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_3 = QScrollArea(self.frame_12)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        sizePolicy.setHeightForWidth(self.scrollArea_3.sizePolicy().hasHeightForWidth())
        self.scrollArea_3.setSizePolicy(sizePolicy)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 404, 439))
        self.verticalLayout_11 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_7 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 35))

        self.verticalLayout_11.addWidget(self.label_7, 0, Qt.AlignTop)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_8.addWidget(self.scrollArea_3)


        self.verticalLayout_5.addWidget(self.frame_12)


        self.horizontalLayout_2.addWidget(self.frame_6)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_13 = QFrame(self.frame)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(16777215, 50))
        self.frame_13.setStyleSheet(u"Border-Top: 3px solid rgba(255,255,255,0.05);\n"
"Border-Bottom: 3px solid rgba(255,255,255,0.05);\n"
"")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pushButton_5 = QPushButton(self.frame_13)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMaximumSize(QSize(30, 16777215))
        self.pushButton_5.setStyleSheet(u"Border: 0px;")
        icon5 = QIcon()
        icon5.addFile(u"icons/sql.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon5)
        self.pushButton_5.setIconSize(QSize(25, 25))

        self.horizontalLayout_6.addWidget(self.pushButton_5)

        self.label_8 = QLabel(self.frame_13)
        self.label_8.setObjectName(u"label_8")
        font3 = QFont()
        font3.setBold(True)
        font3.setWeight(75)
        self.label_8.setFont(font3)
        self.label_8.setStyleSheet(u"Border-Top : 0px;")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_8)

        self.label_9 = QLabel(self.frame_13)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font3)
        self.label_9.setStyleSheet(u"Border-Top : 0px;")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_9)

        self.label_10 = QLabel(self.frame_13)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font3)
        self.label_10.setStyleSheet(u"Border-Top : 0px;")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_10)


        self.verticalLayout_2.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMaximumSize(QSize(16777215, 30))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.pushButton_6 = QPushButton(self.frame_14)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setMaximumSize(QSize(30, 999999))
        icon6 = QIcon()
        icon6.addFile(u"icons/status.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon6)

        self.horizontalLayout_7.addWidget(self.pushButton_6)

        self.label_11 = QLabel(self.frame_14)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(150, 16777215))
        self.label_11.setFont(font3)
        self.label_11.setStyleSheet(u"Border-Right: 3px solid rgba(255,255,255,0.05);\n"
"")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_11)

        self.label_12 = QLabel(self.frame_14)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font3)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_12)


        self.verticalLayout_2.addWidget(self.frame_14)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("Database")
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"DOMAIN SEARCH", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"COUNTRY SEARCH", None))
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"DATABASE ", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"FILTER BY TIME", None))
        self.pushButton_2.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"ANOMALIES LIST", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_3.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"COUNTRIES LIST", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_4.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"CENSORED EVENTS LIST", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_5.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Total Anomalies: 19", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Top Country: AE (19 Events)", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Total Censorship Events: 19", None))
        self.pushButton_6.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Top Domains Censored", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"www.somedomain.com,www.somedomain2.com,www.somedomain3.com", None))
    # retranslateUi

