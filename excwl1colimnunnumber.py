list1=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','D','T','U','V','X','Y','Z']
num=980089
list2=[]
r=0
powq=1
while(powq<num):
    powq*=26
    r+=1
str1=''

for i in range(r-1,-1,-1):
    value=num//26**i
    str1+=list1[value-1]
    num-=(26**i)*value

print(str1)