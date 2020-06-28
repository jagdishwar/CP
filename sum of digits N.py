n=3
s=6
dp=[[0 for i in range(s+1)] for j in range(n+1)]
dp[0][0]=1
print(dp)
for i in range(n):
    for j in range(s):
        for digit in range(10):
            if j+digit<=s:
                dp[i+1][j+digit]+=dp[i][j]
            else:
                break
print(dp)
print(dp[-1][-1])