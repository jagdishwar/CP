print(ord('1')-48)
str1="-6435D56183011M11 648G1 903778065 762 75316456373673B5 334 19885 90668 8 98K X277 9846"
list1=str1.split(' ')
saka=list1[0]
value=0
for i in range(len(saka)):


    if saka[i].isdigit():
         value+=(ord(saka[i])-48)*(10**((len(saka)-1)-i))

print(value)