n=7
sum1=0
while n>1:
   if int(n)&1:
       sum1+=(n - 1) / 2
       n=(n - 1) / 2 + 1
   else:
       n/=2
       sum1+=n

print(int(sum1))
