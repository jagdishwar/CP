list1= [ 12, 121 ]
list2=[]
list3=[]
ele=list(set(list1))
for i in list1:
    for k in ele:
        pass
    


for i in list1:
    if i<10:
        list2.append(i)
    else:
        list3.append(i)
list2.sort()
list3.sort()

def sep_value(pop2):
    input = [pop2]
    output = list(map(int, str(input[0])))
    return output

str1= ""
while len(list2)!=0 and len(list3)!=0:

    pop1=list2[-1]
    pop2=list3[-1]
    output=[]
    output=sep_value(pop2)
    if output[0] < pop1:
        str1+=str(pop1)
        list2.pop()

    else:
        if output[0]==pop1:
            if output[1]>pop1:
                str1+=str(pop2)
                list3.pop()
            else:
                str1+=str(pop1)
                list2.pop()
        else:
            str1+=str(pop2)
            list3.pop()
while len(list3)!=0 or len(list2)!=0:
    if len(list3)!=0:
        ooo=list3.pop()
        str1+=str(ooo)
    if len(list2)!=0:
        oo = list2.pop()
        str1 += str(oo)

print(str1)

