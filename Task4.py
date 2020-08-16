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
# initialize sets
not_telemarketers = set()
possible_telemarketers = set()

# Add possible telemarketing numbers
# to not_telemarketers set
for text in texts:
    for i in range(2):
        not_telemarketers.add(text[i])

# Add sending numbers to possible_telemarketers set
# Add receiving numbers to not_telemarketers set
for call in calls:
    possible_telemarketers.add(call[0])
    not_telemarketers.add(call[1])

# Actual telemarketers
actual_telemarketers = sorted(possible_telemarketers.difference(not_telemarketers))

print("These numbers could be telemarketers: ")
for telemarketer in actual_telemarketers:
    print(telemarketer)
