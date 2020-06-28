list1=[0,1,0]
dict_count={}
maxvalue=0
count=0
for i in range(0, len(list1), 2):
    if i+1<=len(list1)-1:
        if list1[i] != list1[i + 1]:
            count += 1


print(count*2)