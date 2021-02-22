str1="acbcccdc"
char='c'
def dp(str1,char):
    if len(str1)<=0:
        return 0
    if str1[0]==char:
        return 1+dp(str1[1:],char)
    else:
        return dp(str1[1:],char)

print(dp(str1,char))

def dp(i):
    if i>=len(str1):
        return 0

    if str1[i]==char:
        return 1+dp(i+1)
    else:
        return dp(i+1)
print(dp(0))


