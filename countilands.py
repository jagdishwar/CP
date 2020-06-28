def countilands(binarymatrix):
    if len(binarymatrix)==0:
        return 0
    count=0
    for i in range(len(binarymatrix)):
        for j in range(len(binarymatrix[0])):
            if binarymatrix[i][j]=="1":
                recursioncall(i,j,binarymatrix)
                count+=1
    print(count)
def recursioncall(i,j,binarymatrix):
        if i>=len(binarymatrix) or j>=len(binarymatrix[0]) or i<0 or j<0 or binarymatrix[i][j]!=1:
            return
        binarymatrix[i][j]="a"
        recursioncall(i,j-1,binarymatrix)
        recursioncall(i,j+1,binarymatrix)
        recursioncall(i-1,j,binarymatrix)
        recursioncall(i+1,j,binarymatrix)



binaryMatrix =[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
countilands(binaryMatrix)

