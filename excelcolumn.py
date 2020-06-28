list1=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
column=str(27)
power=1
list2=[]
index=0
def peranum(column,index):
            for i in range(len(column)):
                index=int(column)//26**power
                list2.append(list1[index-1])
                return index

print(list2)