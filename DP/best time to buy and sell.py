prices=[7,1,5,3,6,4]
def dp(i):
    if i >= len(prices):
        return 0
    if i + 1 <= len(prices) - 1:
        return max(dp(i + 1), dp(i + 1) + abs(prices[i] - prices[i + 1]))


print(dp(0))