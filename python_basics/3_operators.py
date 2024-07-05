#!/usr/bin/env python

types = (
    'Arithmetic operators',
    'Assignment operators',
    'Comparison operators',
    'Logical operators',
    'Identity operators',
    'Membership operators',
    'Bitwise operators'
)

print("Different types of available operators in python are: ")
for operator_type in types:
    print(operator_type)
print('-'*55)

print(types[0])
a = 11
b = 7
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
print("Floor division:", a // b)
print('-'*55)

print(types[1])
assignment_operators = ('=', '+=', '-=', '*=', '/=', '%=', '**=', '&=', '|=', '^=', '>>=', '<<=', ':=')
print("Examples:")
for operator in assignment_operators:
    print(operator)


print(types[2])
comparision_operators = ('==', '!=', '>', '<', '>=', '<=')
for operator in comparision_operators:
    print('a', operator, 'b')


print(types[3])
print("Examples of logical operators are: and, or, not")

print(type[4])
print("Examples: is, is not")

print(type[5])
print("Examples: in, not in")

print(type[6])
print("Examples:")
print("&  AND")
print("|  OR")
print("^  XOR")
print("~  NOT")
print("<< Zero fill left shift")
print(">> Signed right shift")