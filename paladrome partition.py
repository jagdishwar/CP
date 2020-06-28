def dfspaladrometree(str1,combination,output):
    if len(str1)==0:
        output.append(combination[:])
        return
    else:
        for i in range(len(str1)):
            if valid(str1[:i+1]):
                combination.append(str1[:i+1])
                dfspaladrometree(str1[i+1:], combination, output)
                combination.pop()



def valid(wqord):
    if wqord==wqord[::-1]:
        return True
    return False
output=[]
str1='aab'
dfspaladrometree(str1,[],output)
print(output)
