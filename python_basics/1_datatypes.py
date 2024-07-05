#!/usr/bin/env python3

full_name = "Nikhil Aryal"
number = 42; arko_number = 2538 + number
decimal_number = 25.80
records = [ 2, 4, 6, 8, 12, 14, 18, 22 ]
marks = ( 11, 17, 28, 33, 48, 54, 69 )
sequence = range(33)
data = {
    'name': "Kamal Thapa",
    "district": 'Kaski',
    'position': 'Intern',
    'join_date': '21-05-2023'
}
non_repeated_records = { "apple", "ball", "cat", 'cow', 'cat', 'data', 'dog', 'data' }
is_truth = False  # or, True
content = b'Some content that could also\nInclude non-unicode characters, like binary!'
nothing = None

print(f"Hey guys, my name is {full_name}.")
print(f"I don't know why, but I kinda like number {arko_number}")
print(f"And, sometimes even this number works for me: {decimal_number}0")

records[-1] = 96

print("-"*55)
print("Numbers within list named records:", end=" ", flush=True)
for record in records:
    print(record, end=' ', flush=True)
print()
print("Tuple content:", end=" ", flush=True)
for mark in marks:
    print(mark, end=" ", flush=True)
print()
print("-"*55)

for number in sequence:
    print(number)

print("-"*55)
print(f"{data['name']} is a person working on XYZ workspace, from {data['district']} district as {data['position']} from {data['join_date']}.")
print('-'*55)
print("See, these values are not repeated:")
for entry in non_repeated_records:
    print(entry)
print('-'*55)

if is_truth:
    print("True is set in the variable.")
else:
    print("False is set in the variable.")

print('-'*55)
print(content)
print(content.decode())
print('-'*55)

print(f"Noting is {nothing} in python here..")