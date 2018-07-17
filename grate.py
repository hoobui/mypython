#!/usr/local/bin/python3

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

