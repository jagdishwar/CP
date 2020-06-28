#codechef - lost guy radhu
t=int(input("enter the input please"))
str1,str2=map(int,input("enter the name imout").split(" "))
list2=[]
list3=[]
list4=[]
print(list1)
print(list1[0])
i=0
for z in range(t):
            for i in range(list1[0]):
                  A=int(input("scores in games played "))
                  list2.append(A)
            print(list2)
            for k in range(list1[1]):
                  B=int(input("quries please enter"))
                  list3.append(B)

            print(list3)
            for l in list3:

                      for k in range(l):
                           list4.append(list2[k])
                      print(max(list4))

                      while 1:
                          if i in list4:
                             list4.pop()
                          i+=1
                          break