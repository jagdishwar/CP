list1=[2,1,3,2,3,4,5,1,2,8]
minjump=[0]
list2=[float('inf')]*(len(list1)-1)
minjump.extend(list2)
print(minjump)

for i in range(1,len(list1)):
    for j in range(0,i):
       if j+list1[j]>=i :
           if minjump[i]>minjump[j]+1:
               minjump[i]=minjump[j]+1
print(minjump)