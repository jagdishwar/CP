for i in range(5):
    list1=list(map(int,input().split()))
    flag=0
    for j in range(5):
        if list1[j]==1:
            flag=1
            break
    if flag==1:
        break

print(abs(3-(i+1))+abs(3-(j+1)))

