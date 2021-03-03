"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

def LongestTime(record):
    i = 0
    tempDict = {}   #create empty dictionary
    for elem in record: #iterate through each row of each file
        try:    #try - except to prevent program from crashing    
            if elem[i] not in tempDict: #consider the first column of each row, if num in that index not in tempDict
                tempDict[elem[i]] = elem[i+3]   #append that num into tempDict as a key, the duration of the call is appended as the value
                if elem[i+1] not in tempDict:   #move to consider the next column of each row, if the num of this index not in tempDict, 
                    tempDict[elem[i+1]] = elem[i+3] #append the number and its call duration as key-value pair to tempdict
                else:   #otherwise, if the number of the second column is already existed in tempdict, 
                    tempDict[elem[i+1]] = str(int(tempDict[elem[i+1]]) + int(elem[i+3]))   #add the new call duration to the num's exisiting value. 
            else: #if num in the first column/key already in tempDict, 
                tempDict[elem[i]] = str(int(tempDict[elem[i]]) + int(elem[i+3]))    #add the new call duration to the exisiting value
                if elem[i+1] in tempDict:   #move to the next column, repeat the logic as above
                    tempDict[elem[i+1]] = str(int(tempDict[elem[i+1]]) + int(elem[i+3]))
                else:
                    tempDict[elem[i+1]] = elem[i+3]     
        except: #print message and row if meet unexpected situations
            print("An exception occurred:", elem)
            
        
    res = max(tempDict, key = tempDict.get) #get the key/number that has the max value/call duration
    print(res, "spent the longest time,", tempDict[res], "seconds, on the phone during September 2016.") #print phone num and duration spent on the phone
    return res


LongestTime(calls)
