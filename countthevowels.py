strx="abcdurhef"
vowels={'a','e','i','o','u'}
count=0
for i in strx:
    if i.lower() in vowels:
        count+=1


print(count)