s="(*))"
queue=[]
error=0
for i in s:
    if i is "(":
        queue.append('(')
    elif i is ")":
        if len(queue)==0:
            error-=1
        else:
            queue.pop()
    elif i is "*":
        error+=1

if len(queue)>0:
    error-=len(queue)

if error==0:
    return True
else:
    return False

