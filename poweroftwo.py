def solve(self, A, B):
    list1 = A
    size = len(list1) + int(B)

    if (size % 2 == 0):
        median = (list1[int(size / 2) - 1] +
                  list1[int(size / 2)]) / 2
        return median

    median = list1[int(size / 2)]
    return median