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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

#Part A
def CheckPhoneNum(record):
  i = 0
  tempSet = set() #create empty set
  for elem in record:   #iterate thru each row
    if '(' and ')'in elem[i]: #look for nums that have ( and )
      tempSet.add(elem[i][elem[i].index('(') :elem[i].index(')')+1]) #append the area code including ( and ) to tempSet
    elif elem[i][0] == '7' or elem[i][0] == '8' or elem[i][0] == '9': #look for nums begins with 7,8,9
      tempSet.add(elem[i][:4])  #append area code including first 4 digits to tempSet
    elif elem[i][:3] == '140':  #look for nums starts with 140
      tempSet.add('140')        #append 140 to tempSet
  res = '\n'.join(sorted(tempSet))  #sort tempSet and add line break between each area code
  return res


#Part B
def CheckFixLine(record):
  i = 0
  count = 0
  for elem in record: #iterate thru each row in file
    if '(' and ')'in elem[i] and '(' and ')'in elem[i+1]: #if found a num that has ( and )
      count += 1                                          #add 1 to count
  res = round(float((count/len(record)) * 100),2)         #result: count divided by the total num of records * 100. The end result is rounded up to have 2 decimal digits 
  return res


callRecord = CheckPhoneNum(calls)
print("The numbers called by people in Bangalore have codes:\n", callRecord)

FixLine = CheckFixLine(calls)
print(FixLine, "percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")