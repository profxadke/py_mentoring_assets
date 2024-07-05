#!/usr/bin/env python3

# import sys, requests
import sys
import requests  # Note: you'll have to first `pip install requests`

args = sys.argv[1:]

def display_help(quit=True):
    print("--help\tDisplay this help message.")
    print("--echo\tEchos given argument(s) back to the user.")
    print("--request\tMakes an HTTP request to given URL by user and displays its response body.")
    if quit:
        exit(0)


if '--help' in args or '-h' in args:
    display_help()

if __name__ == '__main__':
    if '--echo' in args or '-e' in args:
        print(' '.join(args[1:]))
    elif '--request' in args or '-r' in args:
        resp = requests.get(args[1])
        print(resp.content.decode())
    else:
        display_help()