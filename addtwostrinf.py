str1="9999999999"
str2='2'

value1=0
value2=0
for i in range(len(str1)):
    value1+=((ord(str1[i])-48)*(10**(len(str1)-(i+1))))
for k in range(len(str2)):
    value2+=((ord(str2[k])-48)*(10**(len(str2)-(k+1))))
print(value1,value2)