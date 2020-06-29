class Solution(object):
    def maxSubArray(self, nums):
        n=len(nums)
        curmax=nums[0]
        res=nums[0]
        for i in range(1,n):
            curmax=max(nums[i]+curmax,nums[i])
            res=max(res,curmax)
            print(i,curmax,res)
        return res

s=Solution()
#arr=[-2,3,-1,2]
arr=[-2,1,-3,4,-1,2,1,-5,4]
print(s.maxSubArray(arr))
