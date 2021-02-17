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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

i = 0
def FindTele(record):
    temp = set()    #create empty set
    for elem in record:
        if elem[i][:3] == "140" and elem[i] not in temp: #look for num starts with 140 in first colum, 
            temp.add(elem[i]) # if that num not in temp, add the num to temp
        if elem[i+1][:3] == "140": #look for num starts with 140 in second column, 
            if elem[i+1] in temp: #if that num already in temp, remove the num from temp
                temp.remove(elem[i+1]) 
            else:               #else, if that num not in temp, add the num to temp
                temp.add(elem[i])
    return temp

Call = FindTele(calls)  #look for all nums with 140 area code in calls
Text = FindTele(texts)  #look for all nums with 140 area code in texts

Telemarketers = '\n'.join(Call.difference(Text)) #get the numbers only show up in Call set, added a line break between each num.

print("These numbers could be telemarketers: ", "\n", Telemarketers)
