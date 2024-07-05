#!/usr/bin/env python3

class Calculator(object):
        def __init__(self, inA, inB):
                self.a = inA
                self.b = inB
        def add(self):
                return self.a + self.b
        def multiply(self):
                return self.a * self.b


class Scientific(Calculator):
        def add(self):
                return super(Scientific, self).add()
        def exponent(self):
                return pow(self.a, self.b)


newCalculation = Calculator(10, 20)

print(f'a + b: {newCalculation.add()}')
print(f'a x b: {newCalculation.multiply()}')

newPower = Scientific(2, 3)

print(f'a + b: {newPower.add()}')
print(f'a * b: {newPower.multiply()}')
print(f'a ^ b: {newPower.exponent()}')
