list1=[1, 2, 3, 4, -10]


max_so_far=list1[0]
max_ending=0
for i in range(len(list1)):
    max_ending=max_ending+list1[i]
    if max_ending>max_so_far:
        max_so_far=max_ending
    if max_ending<0:
        max_ending=0
print(max_so_far)