def minimuminsertiontomakepaladrome(str1,l,h):
    if l==h:
        return 0
    if l>h:
        return float('inf')
    if l==h-1:
        if str1[l]==str1[h]:
            return 0
        else:
            return 1
    if str1[l]==str1[h]:
        return minimuminsertiontomakepaladrome(str1,l+1,h-1)
    else:
        return min(minimuminsertiontomakepaladrome(str1,l+1,h),minimuminsertiontomakepaladrome(str1,l,h-1))+1
print(minimuminsertiontomakepaladrome('banana',0,5))