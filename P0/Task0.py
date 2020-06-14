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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
cpu0=time.clock()
wall0=time.time()

message1="First record of texts, {num1} texts {num2} at time {time}".format(num1=texts[0][0],num2=texts[0][1],time=texts[0][2])
message2="Last record of calls, {num1} calls {num2} at time {time}, lasting {during} seconds".format(num1=calls[-1][0],num2=calls[-1][1],time=calls[-1][2],during=calls[-1][3])
print(message1)
print(message2)

cpu1=time.clock()
wall1=time.time()

print("cpu time is %f s."%(cpu1-cpu0))
print("wall time is %f s."%(wall1-wall0))
