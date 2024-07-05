#!/usr/bin/env python3

# This is how you write single-line comment in Python!
 
print('Hello Python3! 😎')

"""
And, This is how you write a
Multi-line comment in Python!
"""

print('-'*55)

keywords_file = open('keywords.txt')
print(keywords_file.read())
keywords_file.close()