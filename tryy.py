A="A man, a plan, a canal: Panama"

str2=''
for i in A:
    if i.isalpha() or i.isdigit():
        str2+=i.lower()
revstr=''
for j in range(len(str2)-1,-1,-1):
    revstr+=str2[j]

print(revstr)
print(str2)
