s ="anagram"
t="nagarama"
setdict=dict()
ticdict=dict()
for i in s:
    if i in setdict:
        setdict[i]+=1
    else:
        setdict[i]=1

print(setdict)

for i in t:
    if i in ticdict:
        ticdict[i]+=1
    else:
        ticdict[i]=1

print(ticdict)
if setdict==ticdict:
    print('tue')
else:
    print('fuck off')