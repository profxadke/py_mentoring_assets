#!/usr/bin/env python3

from sys import argv

# While, mentoring give example of local and global scopes.

def print5times(line_to_print):
    for _ in range(5):
        print(line_to_print)

example_function = lambda x, y: x ** y

if len(argv) == 2:
    print5times(argv[1])

elif len(argv) > 2:
    print('Only One input Accapted!\n')
    print5times(argv[1])

else:
    inp = input('Enter the input to print 5 times: ')
    print5times(inp)

x, y = 2, 4
print(f'{x} to the power {y} is equal to {example_function(x, y)}')