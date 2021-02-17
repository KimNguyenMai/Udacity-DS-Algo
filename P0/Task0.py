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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
#first record of texts: outgoing num is at first column, incoming num at second column, timestamp at 3rd column of "texts".
#last record of calls: outgoing num is at first column, incoming num at second column, timestamp at 3rd column, length of call at the last column of "calls.

print("First record of texts: ", texts[0][0], "texts ", texts[0][1], "at time: ", texts[0][2])
print("Last record of calls: ", calls[len(calls)-1][0], "calls ", calls[len(calls)-1][1], 
"at time: ", calls[len(calls)-1][2], "lasting ", calls[len(calls)-1][3], "seconds")

