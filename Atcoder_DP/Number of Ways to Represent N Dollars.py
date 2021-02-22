coins=[1,2,5]
amount=5
def dp(amount,prev):
    if amount==0:
        return 1
    res=0
    for i in range(len(coins)):
        if amount-coins[i]>=0 and coins[i]<=prev:
            res=dp(amount-coins[i],coins[i])+res

    return res
print(dp(5,max(coins)))

##^having red flag - combination of [1,2] and [2,1] is counted
coins=[1,2,5]
amount=3
def dp(amount):
    if amount==0:
        return 1
    res=0
    for i in range(len(coins)):
        if amount-coins[i]>=0 :
            res=dp(amount-coins[i])+res

    return res
print(dp(3))
##^if sorted , prev allows previous elements to check , if not sorted then, it allows after element which less than previous
#->element and checking amount offcourse.

#another way
def countways_(bills, amount, index):
  if amount == 0:     # base case 1
    return 1
  if amount < 0 or index >= len(bills):      # base case 2
    return 0
  # count the number of ways to make amount by including bills[index] and excluding bills[index]
  return countways_(bills, amount - bills[index], index) + countways_(bills, amount, index+1)

def countways(bills, amount):
  return countways_(bills, amount, 0)

print(countways([1,2,5], 5))