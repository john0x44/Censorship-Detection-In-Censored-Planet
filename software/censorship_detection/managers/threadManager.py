# creating the thread manager class for handling data processing and loading memory into the machine
# we will utilize qthreads class here for more information we can read the documentation 
# https://doc.qt.io/qt-6/qthread.html


from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCharts import QtCharts
from PySide2 import QtCore, QtGui
from PySide2.QtCore import Qt, QPoint, QSize, Signal, Slot
from PySide2.QtGui import QPen, QColor, QFont

# ProcessBatchThread : Process the batch from each file 
# Return the line amount, fileID, batchData
class ProcessBatchThread(QThread):
    Result = Signal(dict)

    def __init__(self, mainDirectory, datasetDirectory, fileName, fileID, batchSize, iterationSize, lastLineReadPosition):
        QThread.__init__(self)
        self.batch = {} #store the batch 
        self.mainDirectory = mainDirectory
        self.datasetDirectory = datasetDirectory
        self.fileName = fileName
        self.fileID = fileID 
        self.batchSize = batchSize 
        self.iterationSize = iterationSize 
        self.lastLineReadPosition = lastLineReadPosition # store the last line read position
        self.iterationIndex = 1 #store the batch indexing correctly 

    def run(self):
        filePath = f"{self.mainDirectory}/{self.datasetDirectory}/{self.fileName}"
        try:
            with open(filePath, 'r', encoding='utf-8') as file:
                #Move to last read position 
                for _ in range(self.lastLineReadPosition):
                    next(file, None)
            
                for _ in range(self.iterationSize):
                    thisBatch = [] 

                    for _ in range(self.batchSize):
                        line = file.readline()
                        if not line: #if this is the end of file stop
                            break 
                        thisBatch.append(line.strip())
                    
                    if thisBatch:
                        self.batch[self.iterationIndex] = thisBatch
                        self.lastLineReadPosition += len(thisBatch)

                    self.iterationIndex += 1
                        
                    if len(thisBatch) < self.batchSize:
                        break

            # emit the batch fileID, batchSize, lastLineReadPosition
            self.Result.emit({"fileID":self.fileID,"batch":self.batch,"lastLine":self.lastLineReadPosition})

        except Exception as e:
            print(f"Error reading file {self.fileName}: {e}")
        

