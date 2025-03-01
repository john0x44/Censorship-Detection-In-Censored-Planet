# solving the issue of loading in the large dataset since files contain very large datasets which would slow the program down 
# so we utilize the minibatch processing getting small data sets from all files in extracted 

# progress.json file has the progress of each file based on the last gotten batch
from functools import partial 
from threadManager import ProcessBatchThread 
import json 
import os 

class MiniBatch:
    # grab the batch amount and iteration amount since data can change so we have to always check before processing the batches 
    def __init__(self, processBatchButton, getBatchAmount, getIterationAmount): 
        self.processBatchThread = ProcessBatchThread
        self.mainDirectory = "./data" #The directory where we are storing the dataset into 

        self.trackProgressBatch = './data/progress.json' #track the last batch gotten from this file or the lastline
        self.getBatchAmount = getBatchAmount
        self.getIterationAmount = getIterationAmount

        self.processBatchButton = processBatchButton
        self.batchesLoaded = {}
        self.selectedFiles = {} 

        self.batchAmount = 0
        self.iterationAmount = 0 
        self.threadsRunning = 0
        self.processBatchButton.clicked.connect(partial(self.processBatch))

        self.dataProgress = {}

    def processThreadResult(self,batchResult):
        batchesProcessed = []
        self.threadsRunning -= 1 
        batchesProcessed.append(batchResult)

        # we are done with all the threads then we can save the progress of all batches 
        if (self.threadsRunning == 0):
            for i in range(len(batchesProcessed)):
                thisBatch = batchesProcessed[i]
                self.dataProgress[thisBatch['fileID']] = thisBatch['lastLine']
                
                # with open(self.trackProgressBatch, 'w') as file:
                #         json.dump(self.dataProgress, file, indent=4)  

        # print(batchesProcessed) # now we have the loaded batches into memory 
        
    # for each file we create a thread for it so we pass in the file for that thread 
    # need to check in the progress for each batch we produce from the file 
    # we need to pass in the iterations and batch size for each file in each thread, the thread should return the line number from the last batch fetched from 
    
    def getLastLineReadPosition(self,fileID):
        #self.trackProgressBatch = './data/progress.json' #track the last batch gotten from this file or the lastline
        lastLine = 0
        if fileID not in self.dataProgress:
            self.dataProgress[fileID] = 0 
            lastLine = self.dataProgress[fileID]
        else:
            lastLine = self.dataProgress[fileID]
        return lastLine
        # try:
        #     with open(self.trackProgressBatch, 'r') as file:
        #         self.dataProgress = json.load(file)
        #         if len(self.dataProgress) > 0:
        #             return self.dataProgress[str(fileID)]
        #         else:
        #             # add in this fileID into the json file
        #             # If fileID does not exist add into 
        #             if str(fileID) not in self.dataProgress:
        #                 self.dataProgress[str(fileID)] = 0  
        #                 with open(self.trackProgressBatch, 'w') as file:
        #                     json.dump(self.dataProgress, file, indent=4)  
        #             return self.dataProgress[str(fileID)]
                
        # except Exception as e:
        #     print("ERROR",e)

    def processBatch(self):
        # check if we have the selected files 
        self.batchAmount = self.getBatchAmount() 
        self.iterationAmount = self.getIterationAmount()

     
        if len(list(self.selectedFiles)) > 0:
            for fileID in self.selectedFiles: 
                # Create the thread for this 
                self.threadsRunning += 1
                lastLineReadPosition = self.getLastLineReadPosition(fileID)
                processBatchThread = self.processBatchThread(self.mainDirectory,self.selectedFiles[fileID]['DirectoryFrom'],self.selectedFiles[fileID]['FileName'],fileID,self.batchAmount,self.iterationAmount,lastLineReadPosition)
                processBatchThread.Result.connect(self.processThreadResult)
                processBatchThread.run()
        else: 
            pass

    # if the selected files change we need to update this 
    def setSelectedFiles(self, selectedFiles):
        self.selectedFiles = selectedFiles 
