# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboardYxJyEr.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class DashboardUI(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"Dashboard")
        MainWindow.resize(800, 279)
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
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 40))
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
        self.pushButton.setMaximumSize(QSize(40, 16777215))
        self.pushButton.setStyleSheet(u"Border-Bottom: 3px solid rgba(255,255,255,0.05);\n"
"")
        icon = QIcon()
        icon.addFile(u"icons/monitor.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(27, 27))

        self.horizontalLayout.addWidget(self.pushButton)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"Border-Bottom: 3px solid rgba(255,255,255,0.05);\n"
"")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 50))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton_5 = QPushButton(self.frame_6)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMaximumSize(QSize(50, 16777215))
        icon1 = QIcon()
        icon1.addFile(u"icons/sucess.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon1)
        self.pushButton_5.setIconSize(QSize(23, 23))

        self.horizontalLayout_5.addWidget(self.pushButton_5)

        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_5.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_5)


        self.verticalLayout_2.addWidget(self.frame_6)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 110))
        self.frame_4.setStyleSheet(u"Border-Bottom: 3px solid rgba(255,255,255,0.05);\n"
"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.frame_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMaximumSize(QSize(50, 16777215))
        icon2 = QIcon()
        icon2.addFile(u"icons/process.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(23, 23))

        self.horizontalLayout_3.addWidget(self.pushButton_3)

        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 0))
        self.frame_5.setMaximumSize(QSize(16777215, 50))
        self.frame_5.setStyleSheet(u"Border-Bottom: 3px solid rgba(255,255,255,0.05);\n"
"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.frame_5)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMaximumSize(QSize(50, 16777215))
        icon3 = QIcon()
        icon3.addFile(u"icons/error.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QSize(23, 23))

        self.horizontalLayout_4.addWidget(self.pushButton_4)

        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_4)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 50))
        self.frame_3.setStyleSheet(u"Border-Bottom: 3px solid rgba(255,255,255,0.05);\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.frame_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMaximumSize(QSize(50, 16777215))
        icon4 = QIcon()
        icon4.addFile(u"icons/status.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon4)
        self.pushButton_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.label_2)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignTop)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("Dashboard")

        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"DASHBOARD", None))
        self.pushButton_5.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"SUCCESS RATE : 43%", None))
        self.pushButton_3.setText("")
        # self.label_3.setText(QCoreApplication.translate("MainWindow", u"EVENTS PROCESSED: 0/124", None))
        # self.pushButton_4.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"ANOMALIES DETECTED : 0/124", None))
        self.pushButton_2.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"EVENTS DETECTED : 0/124", None))
    # retranslateUi

