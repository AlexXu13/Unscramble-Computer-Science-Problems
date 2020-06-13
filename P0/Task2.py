"""
Read file into texts and calls.
It's ok if you don't understand how to read files
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
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
cpu0=time.clock()
wall0=time.time()

maxnumber1=None
maxnumber2=None
maxtime=0
for record in calls:
    curtime=int(record[-1])
    if curtime > maxtime:
        maxtime=curtime
        maxnumber1=record[0]
        maxnumber2=record[1]
print("{num1} and {num2} spent the longest time, {time} seconds, on the phone during September 2016.".format(num1=maxnumber1,num2=maxnumber2,time=maxtime))
        
cpu1=time.clock()
wall1=time.time()

print("cpu time is %f s."%(cpu1-cpu0))
print("wall time is %f s."%(wall1-wall0))
        
        
        
        