lin=0
i=1
string1='aaabbaaaabaaa'
str1="aaaabaaa"
patt=str1
M=len(patt)-1
lps=[0]*M
while i<M:
    if patt[i]==patt[lin]:
        lps[i]=lin+1
        lin+=1
        i+=1
    else:
        if lin!=0:
            lin=lps[lin-1]
        else:
            lps[i]=0
            i+=1

print(lps)
print((len(str1)-1)-lps[-1])
i=0
j=0
while i<len(string1) and j<len(str1):
    if string1[i]==str1[j]:
        i+=1
        j+=1
    else:
        if j!=0:
            j=lps[j-1]
        else:
            i+=1

    if j==len(str1):
        print(i-j)
        break

