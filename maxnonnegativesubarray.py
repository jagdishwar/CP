list1=[ 1, 2, 5, -7, 2, 5 ]
max_value=0
add_value=0
list2=[]
list3=[]
count=0
if len(list1)>1:

        for i in list1:
            if not i < 0:
                add_value+=i
                list2.append(i)


            if i<0:
                list2.append(0)
                if max_value<add_value:
                    max_value = add_value


        i=0

        while list2[i]!=0:


              count+=list2[i]

              if count==max_value:
                  j=i
                  k=i

                  while list2[k]!=0 and k>=0 :
                      k-=1


                  k=k+1
                  for l in range(k,j+1):
                      list3.append(list1[l])



              i += 1
        print(list3)
else:
    print()