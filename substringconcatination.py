s= "barfoothefoobarman"
t= [ "foo", "bar" ]
if len(t)==0:
    print([])

dict_t={}
ans=[]
l=len(t[0])
for i in t:
    if i in dict_t:
        dict_t[i]+=1
    else:
        dict_t[i]=1
for i in range(l):
    dict_s={}
    left=i
    count=0
    for j in range(i,len(s)-l+1,l):
        char=s[j:j+l]
        if char in dict_t:
            if char in dict_s:
                dict_s[char]+=1
            else:
                dict_s[char]=1
            count+=1
            while dict_s[char]>dict_t[char]:
                dict_s[s[left:left+l]]-=1
                count-=1
                left=left+l
            if count==len(t):
                print(left)
                ans.append(left)
        else:
            left=j+l
            dict_s={}
            count=0
print(ans)



