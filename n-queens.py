
class Solution:
    def solveNQueens(self, n):
        def dfs(nums, row, path, res):
            print('this is row',row)
            if row==len(nums):
                print('hit it up')
                res.append(nums)
                print('this is funcking result ',res)
                return  # backtracking
            for i in range(len(nums)):
                nums[row] = i
                print(nums,'nums')
                print('validity',valid(nums,row))
                print('this is check for the row',row)
                if valid(nums, row):  # pruning
                    tmp = "." * len(nums)
                    dfs(nums, row + 1, path + [tmp[:i] + "Q" + tmp[i + 1:]], res)
                    print('this is funcking path',path)

        # check whether nth queen can be placed in that column
        def valid(nums, row):
            for i in range(row):
                print('this is value abs(nums[i] - nums[row])',nums[i])
                print('this is nums[i]==nums[row]',nums[row])
                if abs(nums[i] - nums[row]) == row - i or nums[i] == nums[row]:#this end statement for the columns.
                    return False
            return True

        res = []
        dfs([-1] * n, 0, [], res)



        print(res)

ob=Solution()
ob.solveNQueens(4)