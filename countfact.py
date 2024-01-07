primes=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

dict1={}

for prime in primes:
    dict1[prime]=2
def countfact(num):

        if num in dict1:

            return dict1[num]

        xnum=num

        count=1

        for prime in primes:

            if num%prime==0:

                c=0

                while num%prime==0:

                    c+=1

                    num//=prime

                count*=c+1

        dict1[xnum]=count

        return count
print(countfact(44))


### prime factorization

def primefactorization(num):
    cnt=2
    prime_divisors=[]
    while cnt*cnt <=num:
        if num%cnt==0:
            ex=0
            while num%cnt==0:
                ex+=1
                num//=cnt
        prime_divisors.append((cnt,ex))
        cnt+=1
    if num!=1:
        prime_divisors.append((num,1))
    return prime_divisors

    
        







    
