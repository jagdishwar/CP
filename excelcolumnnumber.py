list1=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
int1=53
int2=str(int1)
pow1=1
list3=[]
str1=""
lastnumber=1
for i in range(1,len(int2)):
    if lastnumber>0:
            lastnumber = int1 % 26
            list3.append(lastnumber)
            int1 -= lastnumber
    else:
        break
'''    while int1!=0:
        if int1//26**pow1>26:
        
            pow1+=1
        int1=int1//26**pow1
    
        list2.append(int1)
    for i in list2:
        if i!=0:
            i-=1
            str1+=list1[i]
        if i==0:
            str1+=list1[i]
'''

print(list3)