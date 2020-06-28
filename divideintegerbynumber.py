A=-23
B=237
sign=1
if ((A<0)^(B<0)):
   sign=-1
div=abs(345)
dvs=abs(5)
res=0
for i in range(31,-1,-1):
    if div>=(dvs<<i):
        div-=(dvs<<i)
        res+=(1<<i)
print(res*sign)