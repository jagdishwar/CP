matrix=[
  [3, 3, 11, 12, 14],
  [16, 17, 30, 34, 35],
  [45, 48, 49, 50, 52],
  [56, 59, 63, 63, 65],
  [67, 71, 72, 73, 79],
  [80, 84, 85, 85, 88],
  [88, 91, 92, 93, 94],
]

b=94

def binarysearch(b,i):
    l=0
    h=len(i)-1
    while h>l:
        mid=l+h//2
        if i[mid]==b:
            return 1
        else:
            if b<i[mid]:
                h=mid-1
            else:
                l=mid+1
count=0
for i in matrix:
    print(i)

    if len(i)==1 and i[0]==b:

        print (1)
    if len(i)==1 and i[0]!=b:
        count+=1



    if b>i[0] and i[-1]>b:


       if  binarysearch(b,i):
           print(1,'hey you man')
       else:
           print(0,'dixx')

    if count==len(matrix):
        print(0)



