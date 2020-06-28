A=[ 9, -8, -10, -7, 7, -8, 2, -7, 4, 7, 0, -3, -4, -5, -1, -4, 5, 8, 1, 9, -2, 5, 10, -5, -7, -1, -6, 4, 1, -5, 3, 8, -4, -10, -9, -3, 10, 0, 7, 9, -8, 10, -9, 7, 8, 0, 6, -6, -7, 6, -4, 2, 0, 10, 1, -2, 5, -2 ]
A.sort()
list1=A
target=0
result=[]
lx=0
dict1={}
for i in range(len(list1)-2):
      for j in range(i+1,len(list1)-1):
              summ = target - (list1[i] + list1[j])
              print(summ,'isn n siumm')
              for k in range(len(list1[j + 1:])):
                  compl = summ - list1[k]

                  if compl in dict1:
                      result.append([compl, list1[k], list1[j], list1[i]])
                      break
                  elif compl not in dict1:
                      dict1[list1[k]] = i
newresult={}
opeall=[]
for i in result:
    if i not in newresult:
            newresult.add(i)
for k in newresult:
    opeall.append(k)

print(opeall)
