str1='aabaaa'
M=len(str1)-1
lps=[0]*M
list1=[]
i=1
lin=0
while M>i:
    if str1[lin]==str1[i]:
        lps[i]=lin+1
        list1.append(str1[i])
        lin+=1
        i+=1
    else:
        if lin!=0:
            lin=lps[lin-1]
        else:
            lps[i]=0
            i+=1
print(list1)

print(lps)