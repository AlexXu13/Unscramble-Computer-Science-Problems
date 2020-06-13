"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import time
import csv
with open(r'G:/datastructure/P0/P0/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('G:/datastructure/P0/P0/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
cpu0=time.clock()
wall0=time.time()

numlist=[]
for record in texts:
    if record[0] not in numlist:
        numlist.append(record[0])
    if record[1] not in numlist:
        numlist.append(record[0])
for record in calls:
    if record[0] not in numlist:
        numlist.append(record[0])
    if record[1] not in numlist:
        numlist.append(record[0])
print("There are {count} different telephone numbers in the records.".format(count=len(numlist)))

cpu1=time.clock()
wall1=time.time()

print("cpu time is %f s."%(cpu1-cpu0))
print("wall time is %f s."%(wall1-wall0))




