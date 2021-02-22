def print_selected_items(dp, weights, capacity):
    idxes_list = []
    print("Selected weights are: ", end='')
    n = len(weights)
    i = n - 1
    while i >= 0 and capacity >= 0:
        if i > 0 and dp[i][capacity] != dp[i - 1][capacity]:
            # include this item
            idxes_list.append(i)
            capacity -= weights[i]
        elif i == 0 and capacity >= weights[i]:
            # include this item
            idxes_list.append(i)
            capacity -= weights[i]
        else:
            i -= 1
    weights = [weights[idx] for idx in idxes_list]
    print(weights)
    return weights



def solve_knapsack_unbounded_bottomup(profits, weights, capacity):

    n = len(profits)
    # base checks
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0
    dp = [[-1 for _ in range(capacity + 1)] for _ in range(n+1)]
    # populate the capacity=0 columns
    for i in range(n):
        dp[i][0] = 0
    # process all sub-arrays for all capacities
    for i in range(1,n+1):
        for j in range(1, capacity + 1):
            if weights[i - 1] <= j:
                dp[i][j] = max((profits[i - 1] + dp[i][j - weights[i - 1]]), dp[i - 1][j])

            elif weights[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
    # maximum profit will be in the bottom-right corner.
    print(dp[-1][-1])
    print_selected_items(dp, weights, capacity)
    return dp[n - 1][capacity]
weights=[1, 3, 4, 5]
profit=[10, 40, 50, 70]
listprofit=[]
for i in range(len(profit)):
    listprofit.append((weights[i]*profit[i])/100)
capacity=8
solve_knapsack_unbounded_bottomup(profit,weights,capacity)