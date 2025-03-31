# this class manages how the censorship events are shown by color and their score
# green = a non censorship event, red = a censorship event
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

#TODO: remodify show events 
class CreateLabelEvent: 
    def __init__(self, UI, datasetInfo):
        self.UI=UI
        self.score = datasetInfo['score'] 
        self.country = datasetInfo['country']
        self.domain = datasetInfo['domain']

        self.label_4 = QLabel(self.UI.scrollAreaWidgetContents_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 55))
        self.label_4.setStyleSheet(u"Border-Bottom: 3px solid rgba(255,255,255,0.05)")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.UI.verticalLayout_6.addWidget(self.label_4)
        self.UI.verticalLayout_6.setAlignment(Qt.AlignTop)

        self.applyScoreColor()
        self.label_4.setText(f"[DOMAIN:{str.upper(self.domain)}]\n[COUNTRY:{str.upper(self.country)}]\n[SCORE:{str(self.score)}]")

    def applyScoreColor(self):
        normalized_score = max(0, min(1, self.score))  
        transparency = round(normalized_score * 100)  

        if self.score <= 0:  
            rgba = "rgba(255, 0, 0, 1.0)"
        elif self.score >= 1:  
            rgba = "rgba(0, 255, 0, 1.0)"
        else:
            red = round((1 - normalized_score) * 255)
            green = round(normalized_score * 255)
            alpha = 1.0 - (transparency / 100.0)  # Reduce opacity based on transparency
            rgba = f"rgba({red}, {green}, 0, {alpha:.2f})"

        self.label_4.setStyleSheet(f"color: {rgba}; Border-Bottom: 3px solid rgba(255,255,255,0.05);")


class ShowEvents:
    
    def __init__(self, UI, chartManager):
        self.UI = UI 
        self.chartManager = chartManager
    

    def showEvents(self, batches):
        
        filesCount = len(batches)
        datasetsGot = [] 
        for i in range (filesCount):
            # grab each file 
            thisFileBatches = batches[i]['batch']
            batchesLength = len(thisFileBatches)
            # go through each iteration length
            #print(batchesLength)
            for i in range(batchesLength):
                thisBatch = thisFileBatches[i+1]
                #print(thisBatch)
                for x in range(len(thisBatch)):
                    currentBatchScore = thisBatch[x]['score']       
                    currentBatchDomain = thisBatch[x]['domain']
                    currentBatchCountry = thisBatch[x]['server_country']
                    currentBatchStart = thisBatch[x]['start_time']
                    currentBatchEnd = thisBatch[x]['end_time']

                    # we can determine if an event is a censored event by the currentBatchScore anything above 0.5 is considered a censored event anything below 0.49 a non censored event 
                    #       
                    datasetProcessed = {"score":currentBatchScore,"domain":currentBatchDomain,"country":currentBatchCountry,"start":currentBatchStart,"end":currentBatchEnd}
                    datasetsGot.append(datasetProcessed)
                    CreateLabelEvent(self.UI,datasetProcessed)
            # we pass this datasetProcessed to the chartManager here and visualize the chart using the data from datasets got 
            self.chartManager.loadDataset(datasetsGot)