s = "barfoothefoobarman",
words = ["foo","bar"]
lengh=len(words[0])
list1=[]
word=''
count=0
dict_s={}
dict_w={}
result=[]
def continous(result):
    sum1=0
    sum2=0
    for i in range(min(result),max(result)+1):
        sum1+=i
    for i in result:
        sum2+=i
    print(sum2,sum1)
    if sum2==sum1:
        return True
    else:
        return False
for i in range(0,len(s),lengh):
    word=s[i:i+lengh]
    list1.append(word)

for i in words:
    if i in dict_w:
        dict_w[i]+=1
    else:
        dict_w[i]=1
print(list1)
for i in range(len(list1)):
    if list1[i] in dict_s:
        dict_s[list1[i]]+=[i]
    else:
        dict_s[list1[i]]=[i]
print(dict_w)
print(dict_s)
listk=[]
for i in list1:
    if len(result)!=0:
        if result[-1]==i:
            continue
    elif i in dict_s and i in dict_w :
        dict_w[i]-=1
        listk=dict_s[i]
        value=listk[0]
        result.append(value)
        del listk[0]
        dict_s[i]=listk
        print(result,'thats the result')

    if len(result)==len(words):
        if continous(result):
            for key in dict_w:
                dict_w[key]+=1
        else:
            result=[]
            break
        print('got')
    print(dict_w,'suck my dick')



print(result)
