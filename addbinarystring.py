a='11'
b='1'
i=len(a)-1
j=len(b)-1
str1=''
carry=0
while i>=0 or j>=0:
    sum=carry
    if i>=0:
       sum+=int(a[i])
    if j>=0:
       sum+=int(b[j])
    str1+=str(sum%2)
    carry=sum//2
    i-=1
    j-=1
if carry!=0:
    str1+=str(carry)
print(str1[::-1])

