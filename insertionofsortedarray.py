A=[]
B=[]
i=0
j=0
list3=[]
while i<len(A)  and j<len(B):
    if A[i]==B[j]:
        list3.append(B[j])
        i+=1
        j+=1
    elif A[i]<B[j]:
        i+=1
    else:
        j+=1


#++++++++++++++++++++++++++++++++++++
def get_number_of_islands(binaryMatrix):
    # pass # your code goes[0,    1,    0,    1,    0],
    #                     [0,    0,    1,    1,    1],
    #                     [0,    0,    0,    1,    1],
    #                     [1,    0,    0,    0,    1],
    #                     [0,    1,    1,    0,    1],
    #                     [1,    0,    1,    1,    1]
    if not binaryMatrix:
        return []
    count = 0
    # if len(binaryMatrix[0][0])==0:
    #  return 0
    for i in range(len(binaryMatrix)):
        for j in range(len(binaryMatrix[0])):
            if binaryMatrix[i][j] == 1:
                recursioncall(i, j, binaryMatrix)
                count += 1

    return count

    # if element==1
    # recursion


def recursioncall(i, j, binaryMatrix):
    if j >= len(binaryMatrix[0]) or i >= len(binaryMatrix) or j < 0 or i < 0:
        return
    if binaryMatrix[i][j] != 1:
        return

        # checks for i , j

    binaryMatrix[i][j] = ""
    recursioncall(i, j + 1, binaryMatrix)
    recursioncall(i, j - 1, binaryMatrix)
    recursioncall(i + 1, j, binaryMatrix)
    recursioncall(i - 1, j, binaryMatrix)

    # https://leetcode.com/problems/number-of-islands/discuss/56340/Python-Simple-DFS-Solution
