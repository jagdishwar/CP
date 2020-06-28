A=-1324341

str1=str(abs(A))
str2=''
for i in range(len(str1)-1,-1,-1):
    str2+=str1[i]
if abs(int(str2))>2147483648:
    return 0
if A<0:
    return -int(str2)
return int(str2)
