list1=[2,3,1,1,4]
jump=1
steps_down_to=list1[0]
max_go=list1[0]
for i in range(1,len(list1)):
    max_go = max(max_go, list1[i] + i)
    steps_down_to-=1
    if max_go<i:
        print('fsadff')
    if steps_down_to==0:
        jump+=1
        steps_down_to=max_go-i
print(jump-1)

