R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

# Initialize matrix
matrix = []
print("Enter the entries rowwise:")
def call_return(value):
    for i in range(1,value):
        return i
# For user input
for i in range(R):  # A for loop for row entries
    a = []
    for j in range(C):  # A for loop for column entries
        a.append(call_return(R*C))
    matrix.append(a)

# For printing the matrix
for i in range(R):
    for j in range(C):
        print(matrix[i][j], end=" ")
    print()

import numpy as np

R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

print("Enter the entries in a single line (separated by space): ")

# User input of entries in a
# single line separated by space
entries = [i for i in range(1,len(A)**2+1)]

# For printing the matrix
matrix = np.array(entries).reshape(R, C)
print(matrix)