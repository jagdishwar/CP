"""def sudokugamedfs(output,combination,row,matrix):
    if len(combination)==len(matrix[0]):
        output.append(combination[:])
        del combination[:]

    else:
        for rw in range(len(matrix[0])):
            for cl in range(len(matrix[0])):
                if valid(cl+1):_
                combination.append(cl+1)
                sudokugamedfs(output,combination,row+1,matrix)
                combination.pop()


def valid(cl,matrix):
    set1=set()
    for i in combination:
        set1.add(i)

"""

board=[
    [7,8,.,4,.,.,1,2,.],
    [6,.,.,.,7,5,.,.,9],
    [.,.,.,.,.,1,.,7,8],
    [.,.,7,.,4,.,2,6,.],
    [.,.,1,.,5,.,9,3,.],
    [9,.,4,.,6,.,.,.,5],
    [.,7,.,3,.,.,.,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def solvesudoku(board):
    check=findempty(board)
    if not check:
        return True
    else:
        i,j=check
    for k in range(1,10):
        if validposition(board,k,(i,j)):
            board[i][j]=k
            if solvesudoku(board):
                return True
            board[i][j]=0


def validposition(board,num,pos):
    #check row
    for i in range(len(board[0])):
        if board[i][pos[1]]==num and [i]!=pos[0]:
            return False
    #check column
    for j in range(len(board)):
        if board[pos[0]][j]==num and [j]!=pos[1]:
            return False

    #check box

    box_x=pos[0]//3
    box_y=pos[1]//3

    for i in range(box_x*3,box_x*3+3):
        for j in range(box_y*3,box_y*3+3):
            if board[i][j]==num and (i,j)!=pos:
                return False
    return True


def printpatternboard(board):
    for i in range(len(board)):
        if i%3==0 and i!=0:
            print('- - - - - - - - - - - -')
        for j in range(len(board[0])):
            if j%3==0 and j!=0:
                print('| ',end='')

            if j==8:
                print(str(board[i][j]))
            else:
                print(str(board[i][j])  + ' ',end='')



printpatternboard(board)
def findempty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]=='.':
                return(i,j)
    return None



solvesudoku(board)
print('_________________________________________')
printpatternboard(board)