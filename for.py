# abc = {"name":"bob"}
#
# for names in abc:
#     print('%s : %s' % (names,abc[names]))
#
# sum = 0
# for i in range(100):
#     sum += i
# print(sum)

# s = int(input('please input a num: '))
# fib = [0,1]
# for i in range(s):
#     fib.append(fib[-1] + fib[-2])
# print(fib)

# n = int(input('please input a number: '))
# for i in range(1,n+1):
#     for j in range(1,i + 1):
#         print ('%s*%s=%-3s' % (j,i,i*j),end='  ')
#     print()

# print([10 + i for i in range(1,10) if i%2])
#
# f = open('/tmp/passwd')
# # data = f.read(6)
# data1 = f.readlines()
# # print(data)
# print(data1)

# f = open('/tmp/passwd')
# for line in f:
#     print(line,end='')
# f.close()

# f = open('/tmp/myfile','w')
# f.write('like some thing.\n')
# f.flush()


with open('/tmp/passwd') as f:
    print(f.readline())
# print(f.readline())
    print(f.tell())



















