import random

score=int(0)
matrix = [[0 for i in range(4)] for i in range(4)]

#判断是否为空
def notzero(s):
    return s if s != 0 else ''

#显示界面
def showPic():
    print("\r\
          ┌──┬──┬──┬──┐\n\
          │%4s│%4s│%4s│%4s│\n\
          ├──┬──┬──┬──┤\n\
          │%4s│%4s│%4s│%4s│\n\
          ├──┬──┬──┬──┤\n\
          │%4s│%4s│%4s│%4s│\n\
          ├──┬──┬──┬──┤\n\
          │%4s│%4s│%4s│%4s│\n\
          └──┴──┴──┴──┘" \
          % (notzero(matrix[0][0]), notzero(matrix[0][1]), notzero(matrix[0][2]), notzero(matrix[0][3]), \
             notzero(matrix[1][0]), notzero(matrix[1][1]), notzero(matrix[1][2]), notzero(matrix[1][3]), \
             notzero(matrix[2][0]), notzero(matrix[2][1]), notzero(matrix[2][2]), notzero(matrix[2][3]), \
             notzero(matrix[3][0]), notzero(matrix[3][1]), notzero(matrix[3][2]), notzero(matrix[3][3]),)
          )


#游戏初始化
def initGame():
    num=0
    while 1:
        if random.randrange(0, 10)>1:
            s=2
        else:
            s=4
        m = divmod(random.randrange(0, 16), 4)
        if matrix[m[0]][m[1]]==0:
            num+=1
            matrix[m[0]][m[1]]=s
            if num==2:
                break
    showPic()


#判断棋盘是否为空
def checkEmpty():
    for i in range(4):
        for j in range(4):
            if matrix[i][j]==0:
                return True
    return False

#判断游戏是否结束
def check():
    for i in range(4):
        for j in range(3):
            if matrix[i][j] == 0 or matrix[i][j] == matrix[i][j + 1] or matrix[j][i] == matrix[j + 1][i]:
                return True
    else:
        return False

#增加随机数
def AddRandom():  # 处理完移动后添加一个新的随机数
    while 1:
        k = 2 if random.randrange(0, 10) > 1 else 4
        s = divmod(random.randrange(0, 16), 4)
        if matrix[s[0]][s[1]] == 0:
            matrix[s[0]][s[1]] = k
            break
    showPic()


#向左移动
def goLeft():
    global score
    for i in range(4):
        for j in range(3):
            for k in range(1 + j, 4):
                if matrix[i][k] > 0:
                    if matrix[i][j] == 0:
                        matrix[i][j] = matrix[i][k]
                        matrix[i][k] = 0
                    elif matrix[i][j] == matrix[i][k]:
                        matrix[i][j] *= 2
                        score += matrix[i][j]
                        matrix[i][k] = 0
                    break
    if checkEmpty()==True:
        AddRandom()
    else:
        showPic()
    
#向上移动
def goUp():
    global score
    for i in range(4):
        for j in range(3):
            for k in range(j + 1, 4):
                if matrix[k][i] > 0:
                    if matrix[j][i] == 0:
                        matrix[j][i] = matrix[k][i]
                        matrix[k][i] = 0
                    elif matrix[k][i] == matrix[j][i]:
                        matrix[j][i] *= 2
                        score += matrix[j][i]
                        matrix[k][i] = 0
                    break
    if checkEmpty()==True:
        AddRandom()
    else:
        showPic()

#向下移动
def goDown():
    global score
    for i in range(4):
        for j in range(3, 0, -1):
            for k in range(j - 1, -1, -1):
                if matrix[k][i] > 0:
                    if matrix[j][i] == 0:
                        matrix[j][i] = matrix[k][i]
                        matrix[k][i] = 0
                    elif matrix[j][i] == matrix[k][i]:
                        matrix[j][i] *= 2
                        score += matrix[j][i]
                        matrix[k][i] = 0
                    break
    if checkEmpty()==True:
        AddRandom()
    else:
        showPic()

#向右移动
def goRight():
    global score
    for i in range(4):
        for j in range(3, 0, -1):
            for k in range(j - 1, -1, -1):
                if matrix[i][k] > 0:
                    if matrix[i][j] == 0:
                        matrix[i][j] = matrix[i][k]
                        matrix[i][k] = 0
                    elif matrix[i][j] == matrix[i][k]:
                        matrix[i][j] *= 2
                        score += matrix[i][j]  # 将当前数作为score加上
                        matrix[i][k] = 0
                    break
    if checkEmpty()==True:
        AddRandom()
    else:
        showPic()
    
#判断是否获胜
def ifwin():
    for i in range(4):
        for j in range(4):
            if matrix[i][j]==4096:
                return True
    return False
    
def main():
    print("Welcome to the 4096 Game\n");
    initGame();
    while 1:
        print("now your score is ")
        print(score)
        print("Please input the instruction:\n (↑:w) (↓:s) (←:a) (→:d):")
        instr=input()
        if instr=='w':
            goUp()
        elif instr=='s':
            goDown()
        elif instr=='a':
            goLeft()
        elif instr=='d':
            goRight()
        else:
            pass
            print("please follow the correct instructions:\n")
        if not check():
            print("Game over,please try again")
            break
        if ifwin():
            print("Congratulations. You have won!!")
            break

            
    


if __name__ == '__main__':
    main()