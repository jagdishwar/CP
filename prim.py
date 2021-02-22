import math
num=11
def funct(num):

    for i in range(2,int(math.sqrt(num))):
        if num%i==0:
            return False
            break
    return True

print(funct(num))