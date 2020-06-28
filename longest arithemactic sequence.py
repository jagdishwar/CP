list1=[3,6,9,12]
dictlist=[]
maxvalue=0
for _ in range(len(list1)):
    dictlist.append({})
for i in range(len(list1)):
    for j in range(0,i):
        if i==0:
            dictlist[i][j]=0
            break
        diff=list1[i]-list1[j]
        print(dictlist[j])
        if diff in dictlist[j]:
            dictlist[i][diff]=dictlist[j][diff]+1
        else:
            dictlist[i][diff]=2
        print(dictlist)
        if maxvalue<dictlist[i][diff]:
            maxvalue=dictlist[i][diff]
print(maxvalue)
