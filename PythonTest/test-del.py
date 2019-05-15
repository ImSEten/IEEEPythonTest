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
        ###bug
        if count > max:#直接覆盖掉output
            max = count#更新max
            if x + 1 - count == 0:
                if games[x] == 'W':#白队连胜
                    if (count + 2) % 2 == 0:#胜利偶数场，直接保存当前顺序
                        output = [players[0] + ' ' + players[2]]
                    else:#胜利奇数场
                        output = [players[2] + ' ' + players[0]]
                else:#黑队连胜
                    if (count + 2) % 2 == 0:#胜利偶数场，直接保存当前顺序
                        output = [players[1] + ' ' + players[3]]
                    else:#胜利奇数场
                        output = [players[3] + ' ' + players[1]]
            else:
                if games[x] == 'W':#白队连胜
                    if (count + 2) % 2 > 0:#胜利奇数场，直接保存当前顺序
                        output = [players[0] + ' ' + players[2]]
                    else:#胜利偶数场
                        output = [players[2] + ' ' + players[0]]
                else:#黑队连胜
                    if (count + 2) % 2 > 0:#胜利奇数场，直接保存当前顺序
                        output = [players[1] + ' ' + players[3]]
                    else:#胜利偶数场
                        output = [players[3] + ' ' + players[1]]
        elif count == max:#output添加一项
            max = count
            if x + 1 - count == 0:#从第一局开始一直连胜
                #偶数场保存当前顺序，奇数场交换顺序
                if games[x] == 'W':#白队连胜
                    if (count + 2) % 2 == 0:#胜利偶数场，直接保存当前顺序
                        setoutput = players[0] + ' ' + players[2]#当前顺序
                        output.append(setoutput)
                    else:#胜利奇数场，交换顺序
                        setoutput = players[2] + ' ' + players[0]#交换顺序
                        output.append(setoutput)
                else:#黑队连胜
                    if (count + 2) % 2 == 0:#胜利偶数场，直接保存当前顺序
                        setoutput = players[1] + ' ' + players[3]
                        output.append(setoutput)
                    else:#胜利奇数场，交换顺序
                        setoutput = players[3] + ' ' + players[1]
                        output.append(setoutput)
            else:
                if games[x] == 'W':#白队连胜
                    if (count + 2) % 2 > 0:#胜利奇数场，直接保存当前顺序
                        setoutput = players[0] + ' ' + players[2]#当前顺序
                        output.append(setoutput)
                    else:#胜利偶数场，交换顺序
                        setoutput = players[2] + ' ' + players[0]#交换顺序
                        output.append(setoutput)
                else:#黑队连胜
                    if (count + 2) % 2 > 0:#胜利奇数场，直接保存当前顺序
                        setoutput = players[1] + ' ' + players[3]
                        output.append(setoutput)
                    else:#胜利偶数场，交换顺序
                        setoutput = players[3] + ' ' + players[1]
                        output.append(setoutput)
        front = games[x]#更新前一个胜利者
    for x in range(len(output)):
        print(output[x])
FootballDynasty()
