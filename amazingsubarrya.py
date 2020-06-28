str1='ABED'
str2=''
count=0
for i in range(len(str1)):
    if str1[i] in 'aeiouAEIOU':
        count+=(len(str1)-i)


print(count)


