# 1.输出名字年龄
name = input('please input your name: ')
age = input('please input your age: ')

print('name is %s,age is %s' % (name,age))

# 2.输出字符串
print("Tom's pet is a cat.The cat's name is \"Tiechui\"")

# 3.输出列表
s = "Python2best"
s1 = [3,5,4,2]
s2 = []
for i in s:
    s2.append(i)
print(s2)

s2 = s2[:6]
s2.append('3')
print(s2)
s2.append('!')
print(s2)

# 4.创建字典
D = {"name":"Bob","age":"30"}
D["score"] = "90"
D["age"] = "25"
age = D["age"]
print(D)
print("Bob's age is:",age)