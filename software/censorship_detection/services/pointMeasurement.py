# Implement a measurement point system 

# set measurementPoint to 0 if it is closer to 1 (high probability for a censorship event) 
# conditions met 																						Change in measurement point 
# no_response_in_measurement_matches_template = True 		                                            +0.1 
# stateful_block = True 																			    +0.05
# received_status (null,403,451,503...) 												                Based on status codes 
# received_error 																						Based on the text in recieved_error 
# server_country 																						Based on country type (some countries regularly censor content. If data comes from a list of countries, a censorship is more likely) 
# matches_template																				        -0.2 (Hyperquack template process)
# controls_failed 																						-0.2 (False)
# domain_is_control																					    -0.5 (True) 

# stateful_block = True 
# After the first request was sent it was blocked, but a later request was succeeded 
# Might identify temporary censorship or network may be offline 

# recieved_status (null,403,451,503) (Detecting network layer filtering) 

# 403 - Forbidden - User does not have permission to access (+0.1) (Website works but restricted access) 
# 404 - Not Found - Not route found 	(+0.05) (If website is down or user cannot access 
# 451 - Request resource is unavailable due to legal reasons (+0.1) (Government blocking) 
# 503 -  Service unavailable - Server is busy (overloaded,updates,maintenance) (+0.05) (Website is unavailable temporarily, might indicate some network blocking more likely too many clients)
# null - We dont know the network status code - (Website might be down?) (-0.1) 

# Http 400 - status codes Client Errors , 200 - good, 300 - redirection , 500 - server error 

# recieved_error : If there is some sort of error message recieved from the recieved responses 
# contains text "connection reset by peer" - Connection reset by peer suggesting intentional blocking at network level (firewall) (+0.1) 
# contains text "null" - no error - (-0.1) 
# contains text "Incorrect web response: status lines don't match" (+0.1) 
# Several conditions when "HTTP status line returned by the server does not match the expected status line from the template."

# Possible cause 													
# Censorship (content response tampering)  (Server response is modified to alter content) (Possible censorship: +0.1) 
# Combination with other indictors 
# recieved_status code 403,451 or 503 (can increase score) 
# TODO: look for text codes in recieved body 
class PointMeasurement:

    def __init__(self):
        self.calculatingScore = False 

    # analyze a particular batch to get a score for it 
    def calcScore(self, thisBatch):
        if not(self.calculatingScore):
            self.calculatingScore = True
            newScore = 0 
            if thisBatch['stateful_block'] == True:
                newScore += 0.05

            if thisBatch['no_response_in_measurement_matches_template'] == True:
                newScore += 0.1 
            
            if thisBatch['matches_template'] == True:
                newScore += -0.2 
            
            if thisBatch['domain_is_control'] == True:
                newScore += -0.2

            if thisBatch['controls_failed'] == False:
                newScore += -0.2

            # todo: can look for more text in the recieved body
            if thisBatch['received_body'] and "BLOCKED" in thisBatch['received_body']:
                newScore += 0.5 #strong indication that this is censorship 

            # calculate status codes 
            if "received_status" in thisBatch:
                newScore += self.statusCodeScore(str(thisBatch['received_status']))

            if "received_error" in thisBatch: 
                newScore += self.recievedErrorScore(str(thisBatch['received_error']))

            thisBatch['score'] = newScore 

            self.calculatingScore = False 

    def recievedErrorScore(self, errorMsg):
        if "connection reset by peer" in errorMsg:
            return 0.1 
        if "null" in errorMsg:
            return -0.1 
        if "Incorrect web response: status lines don't match" in errorMsg:
            return 0.1 
        return 0.0 
        
    def statusCodeScore(self, statusCode):
        if "403" in statusCode:
            return 0.1
        if "404" in statusCode:
            return 0.05
        if "451" in statusCode:
            return 0.2 
        if "503" in statusCode:
            return 0.05
        if "null" in statusCode:
            return -0.1
        return 0.0