# solving the issue of loading in the large dataset since files contain very large datasets which would slow the program down 
# so we utilize the minibatch processing getting small data sets from all files in extracted 

# progress.json file has the progress of each file based on the last gotten batch
from functools import partial 
from managers.threadManager import ProcessBatchThread 

from services.filtering import Filtering 
from services.showEvents import ShowEvents 
from services.countrySummary import CountrySummary

import json 
import os 
import sys 

class MiniBatch:
    # grab the batch amount and iteration amount since data can change so we have to always check before processing the batches 
    def __init__(self, UI, processBatchButton, getBatchAmount, getIterationAmount, updateBatchesMemSize, chartManager, dashboardManager, databaseManager, scoreReportManager): 
        self.UI = UI 
        # Load managers into memory for use throughout software 
        self.databaseManager = databaseManager
        self.chartManager = chartManager 
        self.scoreReportManager = scoreReportManager 

        self.filtering = Filtering(dashboardManager) 
        self.showEvents = ShowEvents(self.UI, chartManager)
        self.dashboardManager = dashboardManager
        self.countrySummary = CountrySummary()
        self.processBatchThread = ProcessBatchThread
        self.mainDirectory = "./data" #The directory where we are storing the dataset into 

        self.trackProgressBatch = './data/progress.json' #track the last batch gotten from this file or the lastline
        self.getBatchAmount = getBatchAmount
        self.getIterationAmount = getIterationAmount

        self.processBatchButton = processBatchButton
        self.selectedFiles = {} 

        self.batchAmount = 0
        self.iterationAmount = 0 
        self.threadsRunning = 0
        self.processBatchButton.clicked.connect(partial(self.processBatch))
        self.updateBatchesMemSize = updateBatchesMemSize 

        self.processingBatch = False 
        self.dataProgress = {}
        self.batchesMemSize = 0

        self.batchesProcessed = []  #store the batches loaded into memory

        self.currentBatches = [] #store the current batches being processed 


    def processThreadResult(self,batchResult):
        self.threadsRunning -= 1 
        # Before appending the batches we can filter it here 
        filteredBatch = self.filtering.filterBatch(batchResult)
        self.currentBatches.append(filteredBatch)
        
        # we are done with all the threads then we can save the progress of all batches 
        if (self.threadsRunning == 0):
            for i in range(len(self.currentBatches)):
                thisBatch = self.currentBatches[i]
                self.dataProgress[thisBatch['fileID']] = thisBatch['lastLine'] #set the last line read from the file in case of future batches processed
                #calculate the batches memory size 
                self.batchesMemSize = self.batchesMemSize + (sys.getsizeof(thisBatch['batch'])/1024)
                # with open(self.trackProgressBatch, 'w') as file:
                #         json.dump(self.dataProgress, file, indent=4)  
            self.batchesMemSize = round(self.batchesMemSize,2)
            self.updateBatchesMemSize(self.batchesMemSize)
            
            print(f"Loaded batches in memory {self.batchesMemSize}[MB]")
            self.processingBatch = False
            self.batchesProcessed = self.batchesProcessed + self.currentBatches

            all_batches = []

            for batch in self.batchesProcessed:
                if not batch or 'batch' not in batch:
                    continue

                # loop through batches
                for i in range(len(batch['batch'])):
                    sub_batch_key = i + 1
                    if sub_batch_key not in batch['batch']:
                        continue

                    thisBatch = batch['batch'][sub_batch_key]
                    for entry in thisBatch:
                        if entry.get('canUse', False):
                            all_batches.append(entry)

            self.filtering.treeAnalyzer.trainModel(all_batches)

            for batch in self.batchesProcessed:
                if not batch or 'batch' not in batch:
                    continue

                for i in range(len(batch['batch'])):
                    sub_batch_key = i + 1
                    if sub_batch_key not in batch['batch']:
                        continue

                    thisBatch = batch['batch'][sub_batch_key]
                    for entry in thisBatch:
                        if entry.get('canUse', False) and self.filtering.treeAnalyzer.trained:
                            entry['prediction'] = self.filtering.treeAnalyzer.predict(entry)
                        else:
                            entry['prediction'] = "Unknown"
            
            #Country summary events 

            # Update country based censorship count
            for batch in self.batchesProcessed:
                if not batch or 'batch' not in batch:
                    continue
                for i in range(len(batch['batch'])):
                    sub_batch_key = i + 1
                    if sub_batch_key not in batch['batch']:
                        continue
                    thisBatch = batch['batch'][sub_batch_key]
                    for entry in thisBatch:
                        if entry.get("canUse", False):
                            self.countrySummary.update(entry)

            # Print summary to console
            self.countrySummary.printSummary()

            #self.filtering.treeAnalyzer.visualizeTree()
            self.currentBatches = [] 
            self.dashboardManager.updateTopBlockedDomains(self.batchesProcessed)
            self.filtering.updateDashboard()

            self.databaseManager.loadAnomalies(self.filtering.anomalyLogger.getAnomalies())
            self.databaseManager.loadCountries(self.countrySummary.getSummary())
            self.databaseManager.loadCensoredEvents([
                entry for batch in self.batchesProcessed if 'batch' in batch
                for sub_batch in batch['batch'].values()
                for entry in sub_batch if entry.get("score", 0) > 0.5
            ])

            #Pass censored events by measurement score into scoreReportManager 
            censored_events = [
                entry for batch in self.batchesProcessed if 'batch' in batch
                for sub_batch in batch['batch'].values()
                for entry in sub_batch if entry.get("score", 0) > 0.5
            ]
            self.scoreReportManager.collectUserDetectedDomains(censored_events)
            self.scoreReportManager.updateUI()

            print("\n[Recent Anomalies]")
            for a in self.filtering.anomalyLogger.getSummary():
                print(f"Domain: {a['domain']} | Country: {a['server_country']} | Time: {a['timestamp']} | Reason: {a['reason']}")
        # visualize the batches onto the UI 
        self.showEvents.showEvents(self.batchesProcessed)

    # for each file we create a thread for it so we pass in the file for that thread 
    # need to check in the progress for each batch we produce from the file 
    # we need to pass in the iterations and batch size for each file in each thread, the thread should return the line number from the last batch fetched from 
    
    def getLastLineReadPosition(self,fileID):
        #self.trackProgressBatch = './data/progress.json' #track the last batch gotten from this file or the lastline
        lastLine = 0
        fileID = int(fileID)  # Ensure it's an integer
        if fileID not in self.dataProgress:
            self.dataProgress[fileID] = 0
        lastLine = self.dataProgress[fileID]
        return lastLine
    
        #Tracking progress batch 
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
        if not(self.processingBatch):
            self.processingBatch = True 
            # check if we have the selected files 
            self.batchAmount = self.getBatchAmount() 
            self.iterationAmount = self.getIterationAmount()

            self.threadsRunning = len(list(self.selectedFiles))
            if len(list(self.selectedFiles)) > 0:
                for fileID in self.selectedFiles: 
                    # Create the thread for this 
                    lastLineReadPosition = self.getLastLineReadPosition(fileID)
                    processBatchThread = self.processBatchThread(self.mainDirectory,self.selectedFiles[fileID]['DirectoryFrom'],self.selectedFiles[fileID]['FileName'],fileID,self.batchAmount,self.iterationAmount,lastLineReadPosition)
                    processBatchThread.Result.connect(self.processThreadResult)
                    processBatchThread.run()
            else: 
                self.processingBatch = False

    # if the selected files change we need to update this 
    def setSelectedFiles(self, selectedFiles):
        self.selectedFiles = selectedFiles 
