k="abb"
t='#'.join('@{}$'.format(k))
p=[0]*len(t)
c=0
r=0
max=0

for i in range(1,len(t)-1):
    mirror=2*c-i
    if i<r:
        p[i]=min(r-i,p[mirror])
    while t[i+(1+p[i])]==t[i-(1+p[i])]:
        p[i]+=1
    if i+p[i]>r:
        c=i
        r=i+p[i]
    if max<p[i]:
        max=p[i]
        index=i
print(max,index)
start=index-1-max
end=index-1+max
print(k[start//2:end//2])
print(p)
"""maxele=max(p)
print(maxele)
o=0

for i in range(len(p)):
    if maxele==p[i]:
        o=t[i]
        break
index=0
ele=''
for i in range(len(k)):
    if o==k[i]:
        ele=k[i]
        index=i
        break
if ele==2:
    return ele*2
str1=''
high=maxele//2
count=0
for r in range(index+1,len(k)):
    if count<=high:
        str1+=k[r]
        count+=1

print(str1+ele+str1)


print(ele)

ko=t[p.index(max(p))//2]
start=k.index(ko)
str1=''
while start<=max(p)-1:
    str1+=k[start]
    start+=1print(str1)"""