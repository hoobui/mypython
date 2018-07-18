import random
counter = 1
countwin = 0
countlose = 0
countping = 0
while counter <= 3:

    all_chioce = ['石头','剪刀','布']
    win = [['石头','剪刀'],['剪刀','布'],['布','石头']]
    computer = random.choice(all_chioce)
    tip = '''(0) 石头
    (1) 剪刀
    (2) 布
    请出拳 0 | 1 | 2 : '''
    ind = int(input(tip))
    player = all_chioce[ind]

    print('你出: %s,电脑出: %s' % (player,computer))

    if player == computer:
        print('\033[32;1m 平局 \033[0m')
        countping += 1
    elif [player,computer] in win:
        print('\033[31;1m 你赢了 !!! \033[0m')
        counter += 1
        countwin += 1
    else:
        print('\033[31;1m 你输了 !!!! \033[0m')
        counter += 1
        countlose += 1
    if countwin == 2 or countlose == 2:
        break

if countwin == 2 :
    print("\033[31;1m 你总共赢了:",countwin," 你总共输了:",countlose," 平局: ",countping," 所以你赢了 !!! \033[0m")
else:
    print("\033[31;1m 你总共赢了:",countwin," 你总共输了:",countlose," 平局: ",countping," 所以你输了 !!!! \033[0m")
