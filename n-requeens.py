class Solution:
    def Nqueens(self,n):
        def recursionqueen(cols,row,res,patter):
            if row==len(cols):
                res.append(patter)
                return
            for i in range(len(cols)):
                cols[row]=i
                if valid(row,cols):
                    varr="."*len(cols)
                    recursionqueen(cols,row+1,res,patter+[varr[:i]+'Q'+varr[i+1:]])
        def valid(row,cols):
            for j in range(row):
                if abs(cols[j]-cols[row])==row-j or cols[j]==cols[row]:
                    return False
            return True
        res=[]
        recursionqueen([-1]*n,0,res,[])


obj=Solution()
obj.Nqueens(4)
