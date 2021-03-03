"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
 


with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

def CheckPhoneNum(record):
    i = 0
    newset = set()              #create empty set
    res = 0
    for elem in record:         #iterate through each row in the file    
        newset.add(elem[i])     #add the phone num in elem[i] index to newset()
        newset.add(elem[i+1])   #repeat the above step for elem[i+1]. we stop at this index since the phone nums only show up in the first 2 indices of each file

    return newset #return the set of different numbers

textsRecord = CheckPhoneNum(texts)
callsRecord = CheckPhoneNum(calls)
allRecord = textsRecord.union(callsRecord) #combine 2 sets of numbers from 2 records to get different numbers from both files

print("There are", len(allRecord), "different telephone numbers in the records.")

