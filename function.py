from random import randint
def quq(numlist):
    if len(numlist) <2:
        return numlist
    middle=numlist[0]
    small=[]
    large=[]
    for i in numlist[1:]:
        if i < middle:
            small.append(i)
        else:
            large.append(i)

    return quq(small)+[middle]+quq(large)

if __name__ == '__main__':
    alist=[randint(1,100) for i in range(10)]
    print(alist)
    print(quq(alist))
