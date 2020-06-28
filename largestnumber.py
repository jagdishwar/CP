"""list1=[2,4,2,1,4,13,4,14,5]
list1.sort()
str1=""
for i in range(len(list1)-1,-1,-1):
    str1+=str(list1[i])
print("###",str1)
list2=""
list2=sorted(str1)
str2=""
for k in range(len(list2)-1,-1,-1):
    str2+=list2[k]
print(str2)"""
list1=[2,3,1,4,5,8,7,9,34,45,38,99,84]
list2=[9,8,7,6,5,4,3,2,1,0]
list1.sort()
list3=[]
for i in range(len(list1)):
    for j in range(len(list1)-1,-1,-1):
          print(j)
          k = list1[j] % 10
          p = list1[j] // 10
          print(p,k)
          if p==0 and k>=j:
              list3.append(list1[j])
              list1.remove(list1[j])
          if p>=j and k>=0:
              list3.append(list1[j])
              list1.remove(list1[j])


print(list3)








