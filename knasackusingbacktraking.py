def knapsack(list1,tw,maxweight):

    if maxweight>tw:
        return
    for i in range(len(list1)):
            maxweight=+list1[i]
            knapsack(list1,tw,maxweight)


knapsack(list1,tw,maxweight)