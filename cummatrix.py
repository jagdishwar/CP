H,W=map(int,input().split())
matrix=[ input().split() for i in range(H)]

cummatrix=[[0]*W for j in range(H)]
for i in range(H):
    for j in range(W):
        cummatrix[i+1][j+1]=cummatrix[i][j+1]+cummatrix[i+1][j]-cummatrix[i][j]+matrix[i][j]
