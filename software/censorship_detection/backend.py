from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

#class for creating a file frame
class createFileFrame:
    def __init__(self, UI):
        self.UI = UI 
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.frame_4 = QFrame(self.scrollAreaWidgetContents)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 35))
        self.frame_4.setMaximumSize(QSize(16777215, 0))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.frame_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setBold(True)
        font2.setWeight(75)
        self.pushButton_2.setFont(font2)
        self.pushButton_2.setStyleSheet(u"Border-Bottom: 3px solid rgba(255,255,255,0.05);")

        self.horizontalLayout_4.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.frame_4)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMaximumSize(QSize(85, 16777215))
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"Border-Bottom: 3px solid rgba(255,255,255,0.05);")

        self.horizontalLayout_4.addWidget(self.pushButton)


        self.verticalLayout_3.addWidget(self.frame_4, 0, Qt.AlignTop)
        #class for connecting the backend to frontend 

class ConnectUI:
    def __init__(self, UI, fileInfoUI):
        self.UI = UI 
        self.fileInfoUI = fileInfoUI

        #Storing where our "last" batch fetch happened from each dataset 
        self.trackDataSetBatchFile = "./data/progress.json"

        #how many times do we iterate through all the selected dataset in other words how many times do we grab new data from each dataset?
        self.iterations = 1 

        #how much data or sets do we get from each dataset the more the more processing the machine will require 
        self.bacthSize = 500 

        #user selection update this data is changed throughout the use of the software 
        #TODO: make a class for this
        self.filesSelected = 0
        self.fileSelectedTotalSize = 0
        self.countriesSelected = 0
        self.loadedBatchesInMemory = 0