#!/usr/bin/env python3

min_age = 18
while min_age >= 18:
    age = int(input("What is your age? "))

    if age < 18:
        break

    print('Your age is >= 18', end='\n\n')

else:
    print("Not allowed")

print("Out of loop")


print('-'*55)

for i in range(0, 100, 5):  # i is iterator here
    print(i)
else:
    print('100!')
