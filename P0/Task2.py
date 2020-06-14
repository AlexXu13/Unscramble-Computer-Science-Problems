"""
Read file into texts and calls.
It's ok if you don't understand how to read files
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
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
cpu0=time.clock()
wall0=time.time()

code_dict={}
for record in calls:
    if record[0] not in code_dict.keys():
        code_dict[record[0]]=int(record[-1])
    else:
        code_dict[record[0]]+=int(record[-1])
    if record[1] not in code_dict.keys():
        code_dict[record[1]]=int(record[-1])
    else:
        code_dict[record[1]]+=int(record[-1])
code=max(code_dict.items(),key=lambda item:item[1])

print("{num1} spent the longest time, {time} seconds, on the phone during September 2016.".format(num1=code[0],time=code[1]))
        
cpu1=time.clock()
wall1=time.time()

print("cpu time is %f s."%(cpu1-cpu0))
print("wall time is %f s."%(wall1-wall0))
        
        
        
        