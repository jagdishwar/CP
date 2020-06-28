list1=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
str1='ABA'
sum1=0
pow=0
sum2=0
count=0

for i in range(len(str1)-1,-1,-1):
    index=list1.index(str1[i])
    count+=index+1
    power=26**pow
    power=(index+1)*power

    out=(index+1)+power
    sum1+=out
    pow+=1


print(sum1-count)