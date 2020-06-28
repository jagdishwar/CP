def combinationsum2(list2,index,subset,target):
    if target==0:
        list2.append(subtitle[:])
    elif target<0:
        return:
    else:
        for i in range(len(list2)):
            subtitle.append(list2[:])
            combinationsum2(list2,index,target,target-subset[i])
