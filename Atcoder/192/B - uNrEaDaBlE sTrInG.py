strx=input()
flag=0
for i in range(len(strx)):
    if i%2==0 and not strx[i].islower():
        print('No')
        flag=1
        break
    elif i%2!=0 and not strx[i].isupper():
        print('No')
        flag=1
        break
if flag==0:
    print('Yes')