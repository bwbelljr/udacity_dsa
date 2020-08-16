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
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""
# Combine both lists into one
calls_and_texts = calls + texts

# initialize new set which will have all phone numbers
phone_numbers = set()

# iterate over combined list
for column in calls_and_texts:
    # Extract sending/receiving numbers
    # in both calls and texts, these are first
    # two elements of the list
    phone_numbers.add(column[0])
    phone_numbers.add(column[1])

# get length of the unique list of phone numbers
count_unique_numbers = len(phone_numbers)

# print message
print("There are {} different telephone numbers in the records.".\
    format(count_unique_numbers))
