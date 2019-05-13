import math


def HappyTrailsMain():
    num = input()#input函数输入的永远是str类型
    num = int(num)
    parameters = []
    for x in range(num):
        parameters.append(input())#输入一行
        parameters[x] = parameters[x].split()#将每一行的每个元素按空格隔开
        parmlenth = len(parameters[x])#一行有parmlenth个元素
        for y in range(parmlenth):
            parameters[x][y] = int(parameters[x][y])
    print(parameters)#输出元素
    print(parameters[0][0])#访问单个元素
    print(parameters[0][1] - parameters[1][1])
HappyTrailsMain()
