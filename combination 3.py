def combinationsum(cadidates, index, target, sublist, list1):
    if target == 0:
        list1.append(sublist[:])
        return
    if target < 0:
        return
    else:
        for i in range(index, len(cadidates)):
        
            sublist.append(cadidates[i])
            combinationsum(cadidates, i, target - cadidates[i], sublist, list1)
            sublist.pop()


list1 = []
combinationsum(sorted([1,2,3]), 0, 3, [], list1)
print(list1)