num=980089
str1=''
while(num>0):
    num-=1
    str1+=chr(abs(int(num%26)+65))
    num/=26


reversed(str1)
print(str1)