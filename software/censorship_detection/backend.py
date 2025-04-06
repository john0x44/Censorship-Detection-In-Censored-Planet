from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import os 
import re 
from functools import partial 
#import necessary services/managers 
from services.miniBatch import MiniBatch 
from managers.chartManager import ChartManager
from managers.dashboardManager import DashboardManager
from managers.databaseManager import DatabaseManager 

#class for creating a file frame
class createFileFrame:
    def __init__(self, UI, fileMetaData, showFileUI, processFileSelection):
        self.processFileSelection = processFileSelection
        self.showFileUI = showFileUI
        self.fileMetaData = fileMetaData
        self.UI = UI 
        self.selected = False #this file was not selected yet 


        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.UI.scrollArea.sizePolicy().hasHeightForWidth())
        self.frame_4 = QFrame(self.UI.scrollAreaWidgetContents)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 55))
        self.frame_4.setMaximumSize(QSize(16777215,55))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_4.setContentsMargins(0,0,0,0)
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
        self.pushButton.setMaximumSize(QSize(90, 16777215))
        self.pushButton_2.setMinimumSize(QSize(90, 16777215))
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"Border-Bottom: 3px solid rgba(255,255,255,0.05)")

        icon1 = QIcon()
        icon1.addFile(u"icons/file.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.horizontalLayout_4.addWidget(self.pushButton)

        self.UI.verticalLayout_3.addWidget(self.frame_4)
        self.UI.verticalLayout_3.setAlignment(Qt.AlignTop)
        
        self.addUIDetail()
        
        self.pushButton.clicked.connect(partial(self.updateFileSelection))
        self.pushButton.setText("SELECT FILE")
        self.pushButton_2.clicked.connect(partial(self.showFileUI,self.fileMetaData))

    def updateFileSelection(self):
        if(not(self.selected)):
            self.selected = True 
            self.pushButton.setText("UNSELECT")
        else: 
            self.selected = False 
            self.pushButton.setText("SELECT FILE")

        self.processFileSelection(self.fileMetaData['FileID'],self.fileMetaData['DirectoryFrom'],self.selected)

    # add in the metadata visually 
    def addUIDetail(self):
        self.pushButton_2.setText(f"[Dataset: {self.fileMetaData['DirectoryFrom']}][{self.fileMetaData['Country']}]\n[CLICK FOR MORE INFO]")
        

    
#class for connecting the backend to frontend 
class ConnectUI:
    def __init__(self, UI, fileInfoUI, dashboardUI, databaseUI):
        self.databaseUI = databaseUI 
        self.dashboardUI = dashboardUI
        self.UI = UI 
        self.fileInfoUI = fileInfoUI

        # load in the chart manager 
        self.chartManager = ChartManager(self.UI)
        # load the dashboard UI 
        self.dashboardManager = DashboardManager(self.UI, self.dashboardUI)
        self.databaseManager = DatabaseManager(self.databaseUI,self.UI.pushButton_8)
        # create the minibatch file 
        # pass in the process batch button
        self.miniBatch = MiniBatch(self.UI, self.UI.pushButton_3, self.getBatchAmount, self.getIterationAmount, self.updateBatchesMemSize, self.chartManager, self.dashboardManager, self.databaseManager) 

        # iteration input 
        self.iterationInput = self.UI.lineEdit_2
        # batch amount input 
        self.batchAmountInput = self.UI.lineEdit

        #Grab the UI element for later use
        self.dataSetFileInfoLabel = self.UI.label_2

        #Grab the UI element for all file info 
        self.allFilesInfoLabel = self.UI.label_2 

        #Get the bottom UI label from software 
        self.bottomLabelInfo = self.UI.label 

        self.totalFilesInDir = 0
        self.totalFilesMBSize = 0 

        #The directory in which our data set is located 
        self.dataSetFileLocation = "./data/"
        # #Storing where our "last" batch fetch happened from each dataset 
        # self.trackDataSetBatchFile = "./data/progress.json"

        #how many times do we iterate through all the selected dataset in other words how many times do we grab new data from each dataset?
        self.iterations = 1 

        #store the datasets info that we put into the directory data or the metadata from each file 
        self.dataSetsInfo = {} 

        #how much data or sets do we get from each dataset the more the more processing the machine will require 
        self.batchSize = 500 

        #user selection update this data is changed throughout the use of the software 
        #TODO: make a class for this
        self.filesSelected = 0
        self.fileSelectedTotalSize = 0
        self.countriesSelected = 0
        self.loadedBatchesInMemory = 0

        # get data about placed files from data directory 
        self.loadFilesInDirectory()

        # grab inputs from user for batch amount and iteration amount 
        self.iterationInput.returnPressed.connect(partial(self.setIterationAmount))
        self.batchAmountInput.returnPressed.connect(partial(self.setBatchAmount))

        self.selectedFiles = {} #used for selecting/unselecting a file 

        self.selectedFilesCount = 0 
        self.selectedFilesTotalSize = 0.0

        self.batchesMemSize = 0 #the memory of all batches loaded into memory

    def updateBatchesMemSize(self, newBatchesMemSize):
        self.batchesMemSize = newBatchesMemSize 
        self.updateBottomLabelInfo() 

    def getIterationAmount(self):
        return self.iterations
    
    def getBatchAmount(self):
        return self.batchSize 
    
    #update additional info 
    def updateBottomLabelInfo(self):
        self.bottomLabelInfo.setText(f"FILES SELECTED [{self.selectedFilesCount}] | FILES SELECTED TOTAL SIZE [{self.selectedFilesTotalSize}][MB] | COUNTRIES SELECTED [{self.selectedFilesCount}] | BATCH SIZE [{self.batchSize}] | ITERATIONS [{self.iterations}] | TOTAL BATCHES MEM SIZE [{self.batchesMemSize}][MB]")
    
    # returns if the file was selected or not 
    def processFileSelection(self, fileID, DirectoryFrom, isSelected):
        # add to or remove from selected files based on file ID store the necessary file metadata (since some or more information is needed throughout the software)
        if isSelected:
            self.selectedFiles[fileID] = self.dataSetsInfo[DirectoryFrom][fileID]
            print("added selected file")
        else:
            del self.selectedFiles[fileID]
            print("removed selected file")

        #Calculate new total selected files size
        self.selectedFilesCount = len(list(self.selectedFiles))
        self.selectedFilesTotalSize = 0
        if len(list(self.selectedFiles)) > 0:
            for index in self.selectedFiles:
                self.selectedFilesTotalSize = self.selectedFilesTotalSize + self.selectedFiles[index]['MBSize']

        # update minibatch files 
        self.miniBatch.setSelectedFiles(self.selectedFiles)

        self.updateBottomLabelInfo()


    def setIterationAmount(self):   
        self.iterations = int(self.iterationInput.text())
        self.updateBottomLabelInfo()

    def setBatchAmount(self):
        self.batchSize = int(self.batchAmountInput.text())
        
        self.updateBottomLabelInfo()

    # Show the more file info UI 
    def showMoreFileInfoUI(self,ThisFileMetaData):
        self.fileInfoUI.FileMetaData = ThisFileMetaData 
        self.fileInfoUI.updateFileMetaDataUI() 
        self.fileInfoUI.MainWindow.show()

    # Add the dataset metadata into UI 
    # quick load does not require threads
    def processDatasetInfoIntoUI(self):
        for subDir, fileMetaDataList in self.dataSetsInfo.items():
            for fileMetaData in fileMetaDataList:
                # Pass in the metadata to the UI upon each file creation so we can utilize it later
                createFileFrame(self.UI, fileMetaData, self.showMoreFileInfoUI, self.processFileSelection)
                # add addition file metadata such as total file size, total file count 
                self.totalFilesMBSize = self.totalFilesMBSize + fileMetaData['MBSize']
                self.totalFilesInDir = self.totalFilesInDir + 1 

        self.allFilesInfoLabel.setText(f'Total Files In Directory [{self.totalFilesInDir}] \n Total File Size [{self.totalFilesMBSize} MB]')


    # Get the files that are in the data directory and store metadata about them
    def loadFilesInDirectory(self):
        self.dataSetsInfo= {}
        fileID = 0 #set a unique file id for a file
        # Iterate over the subdirectories inside our 'data' folder 
        # check self.dataSetFileLocation to grab the data 
        for subDir in os.scandir(self.dataSetFileLocation):
            if subDir.is_dir():  
                subDirName = subDir.name
                file_list = []

                # Iterate over files inside the subdirectory
                for file in os.scandir(subDir.path):
                    fileName = file.name 
                    country = re.search(r'country_([A-Z]{2})', fileName).group(1)
                    # grab the country from the filename by country using regex

                    if file.is_file():
                        dataFileSizeB = file.stat().st_size 
                        dataFileSizeKB = dataFileSizeB / 1024 
                        dataFileSizeMB = dataFileSizeKB / 1024 
                        file_info = {
                            "FileID" : fileID,
                            "DirectoryFrom": subDirName,
                            "FileName": fileName,
                            "FileDate": subDirName,
                            "KBSize": round(dataFileSizeKB,2),   
                            "MBSize": round(dataFileSizeMB,2),
                            "Country" : country
                        }
                        fileID = fileID + 1 #increment so each file is unique 

                        file_list.append(file_info)

                # Store in dictionary
                self.dataSetsInfo[subDirName] = file_list
                # Load into UI
                self.processDatasetInfoIntoUI()
        

