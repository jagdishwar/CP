s="abcabcbb"
setstring=set()
maxvalue=0
i,j=0,0
while j<len(s):
    if s[j] not in setstring:
        setstring.add(s[j])
        j+=1
        maxvalue=max(maxvalue,len(setstring))
    else:
        setstring.remove(s[i])
        i+=1

print(maxvalue)