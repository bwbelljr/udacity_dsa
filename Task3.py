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

# Part A
###############################################################################
# Import re module
import re

# I assume valid numbers are calling or receiving numbers
# in the calls list

# initialize prefix set
prefix_set = set()

for call in calls:
    # look at sending and receiving numbers
    for i in range(2):
        # fixed lines
        if call[i].startswith('('):
            # extract numbers in parentheses
            prefix = re.match(r"\((\d+)\)\d+", call[i]).group(1)
            prefix_set.add(prefix)
        # mobile numbers
        elif ' ' in call[i]:
            prefix_set.add(call[i][:4])
        # telemarketer' numbers
        elif call[i].startswith('140'):
            prefix_set.add('140')

print("The numbers called by people in Bangalore have codes:")
for prefix in sorted(prefix_set):
    print(prefix)

# Part B
###############################################################################

# initialize counters
num_calls_from_fixed = 0
num_fixed_to_fixed = 0

# iterate through calls
for call in calls:
    # check if calling number starts with (080)
    if call[0].startswith('(080)'):
        num_calls_from_fixed += 1
        # check if receiving number starts with (080)
        if call[1].startswith('(080)'):
            num_fixed_to_fixed += 1

fixed_to_fixed_pct = (num_fixed_to_fixed/num_calls_from_fixed)*100

message = "{} percent of calls from fixed lines in Bangalore\
 are calls to other fixed lines in Bangalore."
print(message.format(round(fixed_to_fixed_pct, 2)))
