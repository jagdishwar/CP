t=['$','@','A','@','B','@','A','@','B','@','A','@','B','@','A','@','&']
p=[0]*len(t)
c=0
r=0
for i in range(1,len(t)-1):
    mirror=2*c-i
    if i<r:
        p[i]=min(r-i,p[mirror])
    while t[i+(1+p[i])]==t[i-(1+p[i])]:
        p[i]+=1
    if i+p[i]>r:
        c=i
        r=i+p[i]



print(p)
print(max(p))