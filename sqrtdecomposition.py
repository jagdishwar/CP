from math import sqrt, ceil
nums=[int(i) for i in input().split()]
n = len(nums)
m = int(sqrt(n))
small_sums = [0] * (ceil(n / m))

def blocks(nums):
        for i in range(n):
            small_sums[i // m] += nums[i]
blocks(nums)
def update(index,val):
        change = val - nums[index]
        small_sums[index // m] += change
        nums[index] = val

def sumRange(left,right):
        result = 0
        s_left = left // m
        s_right = right // m
        # Add all the blocks
        for i in range(s_left, s_right + 1):
            result += small_sums[i]

        if left % m != 0:
            for i in range(s_left * m, left):
                result -= nums[i]

        right_end = min(len(nums), (s_right + 1) * m)
        for i in range(right + 1, right_end):
            result -= nums[i]

        return result

