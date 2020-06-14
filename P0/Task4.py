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

telemarkers=set()
notelemarkers=set()
for record in calls:
    if record[0] not in telemarkers:
        telemarkers.add(record[0])
    if record[1] not in notelemarkers:
        notelemarkers.add(record[1])
for record in texts:
    if record[0] not in notelemarkers:
        notelemarkers.add(record[0])
    if record[1] not in notelemarkers:
        notelemarkers.add(record[1])
telemarkers=list(telemarkers)
for n in telemarkers:
    if n in notelemarkers:
        telemarkers.remove(n)
telemarkers=sorted(telemarkers)
print("These numbers could be telemarketers:\n")
for code in telemarkers:
    print(code)        
        
cpu1=time.clock()
wall1=time.time()

print("cpu time is %f ."%(cpu1-cpu0))
print("wall time is %f ."%(wall1-wall0))
