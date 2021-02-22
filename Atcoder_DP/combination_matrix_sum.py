matrix=[[1,2,3],[4,5,6],[7,8,9]]
def dp(row,col,tally):
    if col>=len(matrix[0]):
        print(tally)
        return 0
    for i in range(0,len(matrix)):
        dp(i,col+1,tally+matrix[i][col])


print(dp(0,0,0))