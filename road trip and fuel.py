from collections import deque
result=[]
def jump(nums,x):
    list1 = nums
    list1 = deque(list1)
    list1.appendleft(x)
    jump = 1
    if len(list1) == 1 and list1[0] == 1:
        return 0
    if list1[0] == 0:
        if len(list1) > 1:
            return -1
        else:
            return 0
    steps_down_to = list1[0]
    max_go = list1[0]
    for i in range(1, len(list1)):
        if i == len(list1) - 1:
            return jump
        max_go = max(max_go, list1[i] + i)
        steps_down_to -= 1
        if steps_down_to == 0:
            jump += 1
            result.append(i)
            steps_down_to = max_go - i

    return (jump)
arr=[3,1,1]
print(jump(arr,2)-1)

for i in range(len(result)):
    result[i]=result[i]-1

print(*result)
2

