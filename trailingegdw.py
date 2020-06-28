def factorialnumber(num):
    if num==1:
        return 1
    return num*factorialnumber(num-1)


factor=factorialnumber(5)
fastr=list(str(factor))

print(fastr.count('0'))

def factorial(num1):
    for i in range(1,num1):
        num1*=i
    return num1
def trealinf(self,A):
    fact=self.factorial(A)
    counter=0
    while True:
        if fact%10==0:
            counter+=1
            fact//=10

        else:
            break

    return counter

