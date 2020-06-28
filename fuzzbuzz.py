list1=[]
A=3
for i in range(1,A+1):
    if i%3==0:
        list1.append('Fizz')
    elif i%5==0:
        list1.append('Buzz')
    else:
        list1.append(i)

print(list1)