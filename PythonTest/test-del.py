def FootballDynasty():
    num = int(input())
    players = []
    players.append(input())
    players = players[0].split()
    games = input()
    gamenum = len(games)
    max = 0
    count = 0
    front = games[0]
    output = []
    for x in range(gamenum):
        same = False
        if games[x] == front:#胜利者与前一个相同
            count = count + 1
        else:#胜利者与前一个不同
            count = 1
        #赢家交换输家换人
        #白队赢
        if games[x] == 'W':
            ###黑队操作换人
            tempchange = players[3]
            players[3] = players[1]
            players[1] = players[4]
            ###白队操作交换
            tempwhite = players[2]
            players[2] = players[0]
            players[0] = tempwhite
        #黑队赢
        else:
            ###白队操作换人
            tempchange = players[2]
            players[2] = players[0]
            players[0] = players[4]
            ###黑队操作交换
            tempblack = players[3]
            players[3] = players[1]
            players[1] = tempblack
        for y in range(4, num - 1):#移位
            players[y] = players[y + 1]
        players[num - 1] = tempchange
        if count >= max:#output添加一项
            max = count
            if games[x] == 'W':#白队连胜
                if (count + 2) % 2 == 0:#胜利偶数场，直接保存当前顺序
                    setoutput = players[0] + ' ' + players[2]#当前顺序
                    for m in range(len(output)):
                        if output[m] == setoutput:
                            same = True#有相同的
                            break
                    if same != True:
                        output.append(setoutput)
                else:#胜利奇数场
                    setoutput = players[2] + ' ' + players[0]#交换顺序
                    for m in range(len(output)):
                        if output[m] == setoutput:#有相同的
                            same = True
                            break
                    if same != True:
                        output.append(setoutput)
            else:#黑队连胜
                if (count + 2) % 2 == 0:#胜利偶数场，直接保存当前顺序
                    setoutput = players[1] + ' ' + players[3]
                    for m in range(len(output)):
                        if output[m] == setoutput:
                            same = True#有相同的
                            break
                    if same != True:
                        output.append(setoutput)
                else:#胜利奇数场
                    setoutput = players[3] + ' ' + players[1]
                    for m in range(len(output)):
                        if output[m] == setoutput:
                            same = True#有相同的
                            break
                    if same != True:
                        output.append(setoutput)
        front = games[x]#更新前一个胜利者
    for x in range(len(output)):
        print(output[x])
FootballDynasty()
