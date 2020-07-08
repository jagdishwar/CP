matrix =[[-2,-3,3],[-5,-10,1],[10,30,-5]]
t = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
t[-1][-1] = matrix[-1][-1]

for i in range(len(matrix) - 1, -1, -1):
    for j in range(len(matrix[0]) - 1, -1, -1):

        if i == len(matrix) - 1 and j == len(matrix[0]) - 1:
            t[i][j] = min(dungeon[i][j], 0)
        elif j == len(matrix[0]) - 1:
            t[i][j] = t[i + 1][j] + matrix[i][j]
            if t[i][j] > 0:
                t[i][j] = 0
        elif i == len(matrix) - 1:
            t[i][j] = t[i][j + 1] + matrix[i][j]
            if t[i][j] > 0:
                t[i][j] = 0

        else:
            result = max(t[i + 1][j], t[i][j + 1])
            t[i][j] = min(result + matrix[i][j], 0)

print(abs(t[0][0]) + 1)






