"""list1 = [1,2,3]
list2=[]
def formationset(list1):
    print(list1)
    if len(list1)==0:
        return [[]]
    ele=list1[0]
    subset=formationset(list1[1:])
    print('this is subset which moves forword',subset)
    result=[]
    for i in subset:
        ss=i[:]
        ss.append(ele)

        result.append(i)
        result.append(ss)
    print('this is result',result)
    return result





print(formationset(list1))"""
list1=[322]+0
print(list1)