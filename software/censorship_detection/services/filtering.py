# [documentation] https://docs.censoredplanet.org/http.html#hyperquack-v2-raw

# condition explanations 

# no_response_in_measurement_matches_template = True 
# "Equals true if the responses from all the trials failed to match the known template." 

# Hyperquack template process 
# Hyperquack sends a request to a non censored website if the response is consistent across multiple tests it is saved as a template or (expected response) 
# Then we use this template to compare websites (that might have censorship events) to this template if the response does not match the template it might be censorship 

# Templates are important since it helps seperate real censorship from normal network changes 
# Detect censorship better - If a response does not match the template it signals possible blocking 


# controls_failed 

# all control probes (requests to well-known, uncensored websites) failed to match the expected template.
# All control probes that are test requests sent to website that should always be accessible, and if those test request fail it means a network problem or server issue not censorship

# domain_is_control 

# Liveness test to check if the network is working properly , a control domain is a known uncesored website to see if the network is working properly 
# If a control domain fails, it likely means a network failure, control domains are not usually blocked since they are general purpose websites that dont need to be restricted 

# Questions to be answered by this class 
# Q: What if dataset contains no recieved status how do we manage?
# Q: What if dataset has missing metadata such as domain, server_ip, server_country?
# Q: How do we standardize timestamp (make more readable)

from datetime import datetime 
from dateutil import parser
import json 
import pytz 

from services.pointMeasurement import PointMeasurement

# Filter class can be executed using qthread? [optional]
class Filtering: 

    def __init__(self):
        self.processingFilter = False
        self.pointMeasurement = PointMeasurement() 

    # We can do the batch processing without thread since we have reasonable amount of data to work with
    def filterBatch(self, origBatch):
        if not(self.processingFilter):
            self.processingFilter = True
            iterations = len(origBatch['batch'])
            for iterationIndex in range(iterations):
                thisBatch = origBatch['batch'][iterationIndex+1]
                batchSize = len(thisBatch)
                for i in range(batchSize): 
                    # we can add a new metadata into this batch before returning it such as if we can use this batch or not 
                    currentBatch = json.loads(thisBatch[i]) # the one we are indexing 
                    if (self.canUseBatch(currentBatch)):
                        # ok we can do further processing 

                        # standardize timestamps 
                        currentBatch['start_time'] = self.standardizeTimeStamp(currentBatch['start_time'])
                        currentBatch['end_time'] = self.standardizeTimeStamp(currentBatch['end_time'])

                        # we can use the pointmeasurement class here 
                        self.pointMeasurement.calcScore(currentBatch)
                    # set the filtered batch back to the dict with a 'canUse' flag 
                    origBatch['batch'][iterationIndex+1][i]=currentBatch
            self.processingFilter = False

            return origBatch
        
    
    def standardizeTimeStamp(self, thisTimeStamp):
        dt = parser.isoparse(thisTimeStamp)  
        dt_utc = dt.astimezone(pytz.UTC)  # Convert to UTC timezone
        return dt_utc.strftime("%Y-%m-%d %H:%M:%S.%f")  # Standard format
    
    # ask basic questions before processing this batch
    def canUseBatch(self,thisBatch):
        # check some fields before doing processing for this batch

        # Are some important datafields missing?
        thisBatch['canUse'] = True 
        # Add a new point measurement datafield 
        thisBatch['score'] = 0.0

        try:
            if len(thisBatch['domain']) == 0 or len(thisBatch['no_response_in_measurement_matches_template']) == 0 or len(thisBatch['stateful_block']) == 0 or len(thisBatch['controls_failed']) == 0 or len(thisBatch['domain_is_control']) == 0:
                thisBatch['canUse'] = False
        except:
            pass

        return thisBatch['canUse']