A="PAYPALISHIRING"
B=3
if B == 1 :
          print(A)
row_ls = [""]*B
print(row_ls)
ans = ""
cur_row = 0
incr = 1
for i in range(len(A)) :
        row_ls[cur_row] += A[i]
        print(row_ls,'this is row ls')
        if cur_row == B-1 :
            incr = -1
        elif cur_row == 0 :
            incr = 1
        cur_row += incr

"".join(row_ls)
print(row_ls)