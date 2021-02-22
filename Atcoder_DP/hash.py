"""n,l,r,x =map(int,input().split())

list1=list(map(int,input().split()))"""

list1=[1,2,3]
list1.sort()
blank=[]
def dp(start,count,blank):
    if count>=2 and blank[-1]-blank[0]>=x and l<=sum(blank)<=r:
        return dp(start+1,count+1,blank)+1

    for i in range(start,n):
        blank.append(i)
        return dp(i+1,count+1,blank)

print(dp(0,0,blank))



res = []
nums=[10,9,12,11]
n,l,r,x=4,5,234,2
nums.sort()

def backtracking(res,start,subset,nums):
            res.append(list(subset))
            for i in range(start,len(nums)):
                subset.append(nums[i])
                backtracking(res,i+1,subset,nums)
                subset.pop()
backtracking(res,0,[],nums)
count=0

for i in range(len(res)):


        if len(res)>1 and l<=sum(res[i])<=r and res[i][-1]-res[i][0]>=x:
            count+=1

print(count)