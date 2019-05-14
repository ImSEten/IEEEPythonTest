import math

def HappyTrailsMain():
    num = input()#input函数输入的永远是str类型
    num = int(num)
    parameters = []
    high = 0
    for x in range(num):
        parameters.append(input())#输入一行
        parameters[x] = parameters[x].split()#将每一行的每个元素按空格隔开
        parmlenth = len(parameters[x])#一行有parmlenth个元素
        for y in range(parmlenth):
            parameters[x][y] = float(parameters[x][y])
        high = high + parameters[x][1] * math.sin(parameters[x][0] / 180. * math.pi)
    high = round(high, 2)
    print(high)

def SquawkVirus():
    inputparm = input().split()
    num = int(inputparm[0])
    users = []
    count = 0
    for x in range(num):
        users.append(SingleUser())
        users[x].selfnum = x
    users[int(inputparm[2])].receive = 1
    users[int(inputparm[2])].send = 0
    connectionnum = int(inputparm[1])
    for x in range(connectionnum):
        connection = input()
        connection = connection.split()
        for y in range(len(connection)):
            connection[y] = int(connection[y])
            if y == 0:
                users[connection[y]].connectnumb.append(int(connection[y + 1]))
            else:
                users[connection[y]].connectnumb.append(int(connection[y - 1]))

    ###算法主体
    for t in range(int(inputparm[3])):#次数t
        for x in range(num):
            users[x].send = users[x].receive
            users[x].receive = 0
        for x in range(num):
            if users[x].send != 0:
                for y in range(len(users[x].connectnumb)):
                    users[users[x].connectnumb[y]].receive = users[users[x].connectnumb[y]].receive + users[x].send
                users[x].send = 0
    for x in range(num):
        count = count + users[x].receive
    print(count)

class SingleUser:
    def __init__(self):
        self.connectnumb = []
    selfnum = -1
    connectnumb = []
    receive = 0
    send = 0

SquawkVirus()


