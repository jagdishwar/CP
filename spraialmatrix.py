import numpy as np
A=4
list1=[i for i in range(1,A**2+1)]

ppp=np.array(list1).reshape(A,A)
print(ppp)
matrix=[]
lst = []
t = 0
b = len(ppp) - 1
l = 0
r = len(ppp[0]) - 1
dir = 0
while(t <= b and l <= r):
            if(dir == 0):
                for i in range(l,r+1):
                    lst.append(ppp[t][i])
                t += 1
            elif(dir == 1):
                for i in range(t,b+1):
                    lst.append(ppp[i][r])
                r -= 1
            elif(dir == 2):
                for i in range(r,l-1,-1):
                    lst.append(ppp[b][i])
                b -= 1
            elif (dir == 3):
                for i in range(b,t-1,-1):
                    lst.append(ppp[i][l])
                l += 1
            dir = (dir + 1) % 4
print(lst)
matrix=np.array(lst).reshape(A,A)
print(matrix)