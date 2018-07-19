import random
import string

# number = [str(e) for e in range(10)]
# lower = list(string.ascii_lowercase)
# upper = list(string.ascii_uppercase)
# all_chr = []
# password = []
# for item in lower:
#     all_chr.append(item)
# for item in upper:
#     all_chr.append(item)
# for item in number:
#     all_chr.append(item)
# while True:
#     n1 = input('请设置你的密码长度: ')
#     if n1.isdigit():
#         n = int(n1)
#         for i in range(n):
#             pa = random.choice(all_chr)
#             password.append(pa)
#         print("你的密码为：", ''.join(password))
#         break
#     else:
#         print('请输入数字！！！')

all_chr = string.ascii_letters + string.digits


def gen_pass(n=8):
    result = ''
    for i in range(n):
        ch = random.choice(all_chr)
        result += ch
    return result


if __name__ == '__main__':
    print(gen_pass())
