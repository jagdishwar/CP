noOfTradesAvailable=4
p=[0.50,0.50,0.50,0.50]
x=[4.00,1.00,2.00,3.00]
y=[4.00,0.50,1.00,1.00]
list1=[p[i]*x[i]-((1-p[i])*y[i]) for i in range(noOfTradesAvailable)]
list1.sort(reverse=True)
print(list1)
for val in range():
    val+=val























"""r=[a[i]*p[i]-b[i]*(1-p[i]) for i in range(n)]
r.sort(reverse=True)
ans=0
for i in range(k):
    if r[i]<=0:
        break
    ans+=r[i]
print("%.2f"%ans)"""