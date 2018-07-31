#! /usr/bin/python3
# pw.py - An insecure password locker program

PASSWORDS = {
    'email': 'Hello_World',
    'blog' : 'hello_world',
    'twitter' : 'twit_hell0_w0rld'
}

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()
account = sys.argv[1]      # First command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print ('There\'s no account named ' + account )
