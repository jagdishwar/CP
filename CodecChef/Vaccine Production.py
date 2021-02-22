d1,v1,d2,v2,p=map(int,input().split())
maxvalue=max(d1,d2)
minvalue=min(d1,d2)

count=0
val=0
for i in range(min(d1,d2),p):
    if val>=p:
        break
    if i>=maxvalue:
        val+=v1+v2
        count+=1
    else:
        val+=v1
        count+=1

print((1-minvalue)+count)







