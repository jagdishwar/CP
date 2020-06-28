s="a#c"
t="b"
queue1=[]
queue2=[]
for i in range(len(s)):
    if s[i]!="#":
        queue1.append(s[i])
    elif s[i]=="#":
        queue1.pop()
for i in range(len(t)):
    if t[i]!="#":
        queue2.append(t[i])
    elif t[i]=="#":
        queue2.pop()

if queue1==queue2:
    print("true")
else:
    print("false")

