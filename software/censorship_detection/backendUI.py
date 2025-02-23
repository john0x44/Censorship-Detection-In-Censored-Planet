# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainPAGCxC.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1434, 597)
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
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(250, 16777215))
        self.frame_2.setStyleSheet(u"Border-Right: 3px solid rgba(255,255,255,0.05);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        self.frame_6.setFont(font)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"Border-Right: 0px;\n"
"Border-Bottom: 3px solid rgba(255,255,255,0.05);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_2)


        self.verticalLayout_2.addWidget(self.frame_6)

        self.scrollArea = QScrollArea(self.frame_2)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setStyleSheet(u"Border-Right: 0px;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 247, 503))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        # self.frame_4 = QFrame(self.scrollAreaWidgetContents)
        # self.frame_4.setObjectName(u"frame_4")
        # self.frame_4.setMinimumSize(QSize(0, 35))
        # self.frame_4.setMaximumSize(QSize(16777215, 0))
        # self.frame_4.setFrameShape(QFrame.StyledPanel)
        # self.frame_4.setFrameShadow(QFrame.Raised)
        # self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        # self.horizontalLayout_4.setSpacing(0)
        # self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        # self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        # self.pushButton_2 = QPushButton(self.frame_4)
        # self.pushButton_2.setObjectName(u"pushButton_2")
        # sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        # self.pushButton_2.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setBold(True)
        font2.setWeight(75)
        # self.pushButton_2.setFont(font2)
        # self.pushButton_2.setStyleSheet(u"Border-Bottom: 3px solid rgba(255,255,255,0.05);")

        # self.horizontalLayout_4.addWidget(self.pushButton_2)

        # self.pushButton = QPushButton(self.frame_4)
        # self.pushButton.setObjectName(u"pushButton")
        # sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        # self.pushButton.setSizePolicy(sizePolicy)
        # self.pushButton.setMaximumSize(QSize(85, 16777215))
        # self.pushButton.setFont(font2)
        # self.pushButton.setStyleSheet(u"Border-Bottom: 3px solid rgba(255,255,255,0.05);")

        # self.horizontalLayout_4.addWidget(self.pushButton)


        # self.verticalLayout_3.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.topBar = QFrame(self.frame_3)
        self.topBar.setObjectName(u"topBar")
        self.topBar.setMaximumSize(QSize(16777215, 40))
        self.topBar.setStyleSheet(u"Border-Bottom: 3px solid rgba(255,255,255,0.05);")
        self.topBar.setFrameShape(QFrame.StyledPanel)
        self.topBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.topBar)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.topBar)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"Border-Bottom: 0px;\n"
"Border-Right: 3px solid rgba(255,255,255,0.02);\n"
"Border-Left: 0px;")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.pushButton_3 = QPushButton(self.topBar)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMaximumSize(QSize(122, 16777215))
        self.pushButton_3.setFont(font2)
        self.pushButton_3.setStyleSheet(u"Border-Bottom: 0px;")
        icon = QIcon()
        icon.addFile(u"./icons/process.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.pushButton_3)


        self.verticalLayout_5.addWidget(self.topBar)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5.addWidget(self.frame_5)


        self.horizontalLayout.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 30))
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"Border-Top: 3px solid rgba(255,255,255,0.05);")

        self.verticalLayout.addWidget(self.label_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Total Files Loaded [10] \n"
" Total File Size [10 MB]", None))
        #self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"FILE [1] INFO", None))
        #self.pushButton.setText(QCoreApplication.translate("MainWindow", u"SELECT FILE", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u" Files Selected [2] | Files Selected Total Size [10MB] | Countries Selected [1] | Batch Process [500] | Iterations [1] | Loaded Batches In Memory [0 MB]", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"LOAD BATCH", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"STATUS [PROCESSING BATCH]", None))
    # retranslateUi

