import random
import string
number = [str(e) for e in range(10)]
lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)
all_chr = []
password = []
def allchar():
    for item in lower:
        all_chr.append(item)
    for item in upper:
        all_chr.append(item)
    for item in number:
        all_chr.append(item)
allchar()
while True:
    n1 = input('请设置你的密码长度: ')
    if n1.isdigit():
        n = int(n1)
        for i in range(n):
            pa = random.choice(all_chr)
            password.append(pa)
        print(''.join(password))
        break
    else:
        print('请输入数字！！！')