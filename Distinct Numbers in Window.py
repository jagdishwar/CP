
A=[1, 2, 1, 3, 4, 3]
k=3
list1=[]
hash={}
for i in range(k):
    if A[i] in hash:
        hash[A[i]]+=1
    else:
        hash[A[i]]=1

list1.append(len(hash))
print(hash)
for i in range(1,len(A)-k+1):

    removeele=i-1
    newele=i+k-1
    hash[A[removeele]]-=1
    if hash[A[removeele]]==0:
        del hash[A[removeele]]

    if A[newele] in hash:
        hash[A[newele]]+=1
    else:
        hash[A[newele]]=1
    list1.append(len(hash))


print(list1)
