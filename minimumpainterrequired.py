def numberOfPainters(arr, n, maxLen):
    total = 0
    numPainters = 1
    print('maxlength',maxLen)
    for i in arr:
        print('pint iii',i)
        total += i
        print(total,'total')

        if (total > maxLen):
            # for next count
            total = i
            numPainters += 1
            print(numPainters,'numpainter')

    return numPainters


def partition(arr, n, k):
    lo = max(arr)
    hi = sum(arr)

    while (lo < hi):
        mid = lo + (hi - lo) / 2
        print(mid,'mid')
        requiredPainters = numberOfPainters(arr, n, mid)

        # find better optimum in lower half
        # here mid is included because we
        # may not get anything better
        print(requiredPainters,'painter')
        if (requiredPainters <= k):
            hi = mid

            # find better optimum in upper half
        # here mid is excluded because it gives
        # required Painters > k, which is invalid
        else:
            lo = mid + 1

    # required
    return lo


# Driver code
arr = [1,2,3]
n = len(arr)
k = 2
print(int(partition(arr, n, k)))
