# import os
# dir = os.listdir('/opt')
# print(dir)
#
# # cmd = 'ifconfig'
# #
# # state = os.system(cmd)
# # print(state)

# import getpass
#
# username = input("username: ")
# password = getpass.getpass("password: ")
# if username == "bob" and password == "123":
#     print("login successful")
# else:
#     print("login failed")
#

# import random
#
# num = random.randint(1,5)
# a1 = 0
# while a1 < 3:
#   an = int(input("input a num in 1~5: "))
#
#
#   if an > num:
#     print("big")
#   elif an < num:
#     print("small")
#   else:
#     print("right")
#   if an == num:
#       break
#   a1 += 1
# print("the num is ",num)

grade = int(input('please input your grade: '))
if grade > 100:
    print('please input range in 1~100')
else:
    if grade >= 90:
        print('优秀')
    elif grade >= 80:
        print('好')
    elif grade >= 70:
        print('良好')
    elif grade >= 60:
        print('及格')
    else:
        print('努力')
