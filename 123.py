#!/usr/local/bin/python3
# import getpass
# username = input("username: ")
# password = getpass.getpass("password: ")
# if username == "bob" and password == "123":
#     print("login successful")
# else:
#     print("login failed")
number=int(input('number:'))
from random import choice
import string
def genpassword(length=number,a=string.ascii_letters+string.digits):
    return ''.join([choice(a) for j in range(length)])
if __name__=="__main__":
     print(genpassword(number))
