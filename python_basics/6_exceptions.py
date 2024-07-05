#!/usr/bin/env python3

try:
    exception = 0/0

except ZeroDivisionError:
    print('Divided by zero... 😒')

    try:
        while 1:
            pass

    except KeyboardInterrupt:
        print('\b\b'+'Exitting...')

except Exception as exptn:
    print(f'Unknown Error: {exptn}')
