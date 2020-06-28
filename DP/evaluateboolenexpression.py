memo={}
def solve(str1,i,j,istrue):
    if i>j:
        return False
    if i==j:
        if istrue:
            return str1[i]=='T'
        else:
            return str1[i]=='F'
    if (i,j,istrue) in memo:
        return memo[(i,j,istrue)]
    count=0
    for k in range(i+1,j,2):
        print('start time')
        lt=solve(str1,i,k-1,True)
        lf=solve(str1,i,k-1,False)
        rt=solve(str1,k+1,j,True)
        rf=solve(str1,k+1,j,False)
        print('thats the time')
        if str1[k]=='&':
            if istrue:
                 count+=lt*rt
            else:
                 count+=lt*rf+lf*rt+lf*rf
        elif str1[k]=='|':
            if istrue:
                 count+=lf*rt+lt*rf+lt*rt
            else:
                count+=lf*rf
        elif str1[k]=='^':
            if istrue:
                count+=lf*rt+lt*rf
            else:
                count+=lf*rf+lt*rt
        memo[(i,j,istrue)]=count


    return memo[(i,j,istrue)]

str1=['T', '|', 'T', '&', 'F', '^', 'T']
i=0
j=len(str1)-1
istrue=True
value=solve(str1,i,j,istrue)
print(value)

