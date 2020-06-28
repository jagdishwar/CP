s = "ADOBECODEBANC"
t='ABC'
dict_t={}
for i in t:
    if i in dict_t:
        dict_t[i]+=1
    else:
        dict_t[i]=1
left,right=0,0
reqiured=len(dict_t)
window_dict={}
formed=0
index1,index2=0,0
length=float('inf')
while left<len(s) and right<len(s):
    character=s[right]
    if character in window_dict:
        window_dict[character]+=1
    else:
        window_dict[character]=1
    if character in dict_t and window_dict[character]==dict_t[character]:
        formed+=1
    while formed==reqiured and left<=right:
        chrin=s[left]
        inlan = (right - left + 1)
        if inlan < length:
            length = inlan
            index1 = left
            index2 = right
        window_dict[chrin]-=1
        if chrin in dict_t and window_dict[chrin]<dict_t[chrin]:
            formed-=1
        left+=1
    right+=1

print(s[index1:index2+1])