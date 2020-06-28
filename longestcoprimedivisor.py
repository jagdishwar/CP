def computegcd(a,b):
    if b==0:
        return a
    return computegcd(b,a%b)



num1=90
num2=47
if num1<=num2:
    small=num1
    large=num2

else:
    small=num2
    large=num1

print(large ,small)
for i in range(1,large):
    if large%i==0 and computegcd(i,small)==1:
        print(i)