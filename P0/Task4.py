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
cpu0=time.clock()
wall0=time.time()

telemarkets=set()
for record in calls:   
    telemarkets.add(record[0])
for record in calls:
    telemarkets.discard(record[1])
for record in texts:
    telemarkets.discard(record[0])
    telemarkets.discard(record[1])
telemarkers=sorted(list(telemarkets))
print("These numbers could be telemarketers:\n")
for code in telemarkers:
    print(code)        
        
cpu1=time.clock()
wall1=time.time()

print("cpu time is %f ."%(cpu1-cpu0))
print("wall time is %f ."%(wall1-wall0))
