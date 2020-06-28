num = 28
power = 1
r = 0
print(ord('A'))
while(power<num):
    power*=26
    r+=1
rem = ''
for i in range(0,r):
    temp=(num//(26**(r-i)))
    if(temp>0):
        rem+=chr(temp+64)
    else:
        rem+=chr(num+64)

    num = 26**(r-i)-temp
    print(num)
print(rem)

