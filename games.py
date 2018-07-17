# import random
# all_choice = ["shitou","jiandao","bu"]
# computer = random.choice(all_choice)
# play = input("please choice one: ")
# print("your chioce: %s,computer chioce %s" % (play,computer))
#
# if play == "shitou":
#     if computer == 'shitou':
#         print("ping")
#     elif computer == 'jiandao':
#         print('win!!')
#     else:
#         print('lose!!')
# elif play == 'jiandao':
#     if computer == 'shitou':
#         print("lose!!")
#     elif computer == 'jiandao':
#         print('ping')
#     else:
#         print('win!!')
# else:
#     if computer == 'shitou':
#         print("win!!")
#     elif computer == 'jiandao':
#         print('lose!!')
#     else:
#         print('ping')


import random

all_chioce = ['shitou','jiandao','bu']
win = [['shitou','jiandao'],['jiandao','bu'],['bu','shitou']]
computer = random.choice(all_chioce)
tip = '''(0) shitou
(1) jiandao
(2) bu
please input your chioce 0 \ 1 \ 2:'''
ind = int(input(tip))
player = all_chioce[ind]

print('your chioce: %s,computer chioce: %s' % (player,computer))

if player == computer:
    print('\033[32;1m ping \033[0m')
elif [player,computer] in win:
    print('\033[31;1m you win !!! \033[0m')
else:
    print('\033[31;1m you lose !!!! \033[0m')