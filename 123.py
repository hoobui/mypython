#!/usr/local/bin/python3
import getpass
username = input("username: ")
password = getpass.getpass("password: ")
if username == "bob" and password == "123":
    print("login successful")
else:
    print("login failed")
