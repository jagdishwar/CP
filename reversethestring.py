str1="the sky is blue"
list1=list(str1.split(' '))
revstr=''
for i in range(len(list1)-1,-1,-1):
    if i>0:
        revstr+=(list1[i]+' ')
    else:
        revstr+=list1[i]



print(revstr)