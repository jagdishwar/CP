board=[["8","3",".",".","7",".",".",".","."],
       ["6",".",".","1","9","5",".",".","."],
       [".","9","8",".",".",".",".","6","."],
       ["8",".",".",".","6",".",".",".","3"],
       ["4",".",".","8",".","3",".",".","1"],
       ["7",".",".",".","2",".",".",".","6"],
       [".","6",".",".",".",".","2","8","."],
       [".",".",".","4","1","9",".",".","5"],
       [".",".",".",".","8",".",".","7","9"]]
rowvisit = [set() for i in range(len(board))]
colvisit = [set() for i in range(len(board[0]))]
boxvisit = [set() for i in range(len(board))]
for i in range(len(board)):
       for j in range(len(board[0])):
              if board[i][j]!='.':
                     noofbox=(j//3)*3+i%3
                     #for rows checking
                     if board[i][j] not in rowvisit[i]:
                            rowvisit[i].add(board[i][j])
                     else:
                            return False
                     #for cols checking
                     if board[i][j] not in colvisit[j]:
                            colvisit[j].add(board[i][j])
                     else:
                            return False
                     if board[i][j] not in boxvisit[k]:
                            boxvisit[k].add(board[i][j])
                     else:
                            return False


