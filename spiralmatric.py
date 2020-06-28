


matrix=[
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
]
        m,n=len(A)-1,len(A[0])-1
        last_row=m
        last_col=n
        list2=[]
        k=0
        l=0
        dir=0
        while (k<=last_row and l<=last_col):
            if (dir==0):

                for i in range(l,last_col+1):
                    list2.append(A[k][i])
                k+=1
            elif(dir==1):

                for i in range(k,last_row+1):
                    list2.append(A[i][last_col])
                last_col-=1
            elif(dir==2):
                for i in range(last_col,l-1,-1):
                    list2.append(A[last_row][i])
                last_row-=1
            elif(dir==3):
                for i in range(last_row,k-1,-1):
                    list2.append(A[i][l])
                l+=1
            dir=(dir+1)%4

        return list2
