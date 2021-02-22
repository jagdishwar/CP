def dfsdeploy(str1, A, i):
    if i == :
        return
    print(str1)

    dp1 = str1 + "0"
    dp2 = str1 + "1"
    dfsdeploy(dp1, A, i + 1)
    dfsdeploy(dp2, A, i + 1)

A=1
str1 = str(A)
i = 1
dfsdeploy(str1, A, i)
