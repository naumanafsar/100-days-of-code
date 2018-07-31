# An Insecure Password Locker

##Description
As the name says, it's an insecure Password locker, you store your accounts and password in a python dictionary in pw.py file. Whenever you need your password for an account you just simply run the program and it copy your password into your clipboard. It helps a lot if you have different passwords for different accounts and your passwords are lengthy.

## Pre-reqs
In order to make it work, you need to install a python library called 'pyperclip' first.
You can install it by using pip:
`pip insatll pyperclip`

## Run The Program

The program needs only one argument, which is your account name.
For example, if you need to copy your twitter password to your clipboard, you just run the following command:
`./pw.py twitter`
Your twitter password is copied to your clipboard. Now you can paste it anywhere by using `CTRL + V`
