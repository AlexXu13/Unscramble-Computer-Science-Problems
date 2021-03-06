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
cpu0=time.clock()
wall0=time.time()
#partA
code_list=set()
fixedcount=0
totalcount=0
for record in calls:
    if "(080)" in record[0]:
        totalcount+=1
        if record[1][:3]=="140":
            code_list.add("140")
        elif " " in record[1]:
            code_list.add(record[1][:4])
        else:
            code_list.add(record[1].split(')')[0][1:])
            if "(080)" in record[1]:
                fixedcount +=1
code_set=sorted(list(code_list))
print("The numbers called by people in Bangalore have codes:\n")
for code in code_set:
    print(code)
#partB
print("{per:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(per=fixedcount/totalcount*100))


cpu1=time.clock()
wall1=time.time()

print("cpu time is %f s."%(cpu1-cpu0))
print("wall time is %f s."%(wall1-wall0))








