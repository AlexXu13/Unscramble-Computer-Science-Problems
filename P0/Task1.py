"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import time
import csv
with open('./texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('./calls.csv', 'r') as f:
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

numlist=set()
for record in texts:
    numlist.add(record[0])
    numlist.add(record[1])
for record in calls:
    numlist.add(record[0])
    numlist.add(record[1])
print("There are {count} different telephone numbers in the records.".format(count=len(numlist)))

cpu1=time.clock()
wall1=time.time()

print("cpu time is %f s."%(cpu1-cpu0))
print("wall time is %f s."%(wall1-wall0))




