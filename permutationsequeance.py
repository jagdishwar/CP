def dfspermutationsall(list12,resulte,indexs,combination,count,k):
    if len(combination)==len(list12):
        if k==count:
            resulte =combination[:]
        return
    for i in range(len(list12)):
            if i not in indexs:
                indexs.add(i)
                combination.append(list12[i])
                count += 1
                dfspermutationsall(list12,resulte,indexs,combination,count,k)
                indexs.remove(i)
                combination.pop()


list12=[]
n=3
for i in range(1,n+1):
    list12.append(str(i))
resulte=[]
indexs=set()
dfspermutationsall(list12,resulte,indexs,[],0,3)
k=3
print(resulte)
