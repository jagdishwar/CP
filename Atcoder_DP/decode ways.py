"""def dp(i):
    if i>=len(s):
        return 0
    if 0<int(s[i])<=26:
        res=1+dp(i+1)
    if i+1<len(s) and 0<int(s[i:i+2])<=26:
        res=1+dp(i+2)+res

    return res

print(dp(0))"""
#it doesn;t work beacause of question want which answer

s='226'
def dp(s):
    if not s:
        return 1
    if s[0] == "0":
        return 0

    res = 0
    res = dp(s[1:])+res

    if len(s) >= 2:
        if int(s[0:2]) <= 26:
            res = dp(s[2:])+res

    return res


print(dp(s))