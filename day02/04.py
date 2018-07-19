def myfunction(x):
    if x > 0:
        print(x,'是正数')
        return x
    else:
        print(x,'是负数或者0')
        return x
print(myfunction(5))
print(myfunction(-3))