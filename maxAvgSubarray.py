class Solution(object):
    def findMaxAverage(self, nums, k):
        n=len(nums)
        res=0
        sum=0
        for i in range(0,k):
            sum+=nums[i]
        res=float(sum)
        for j in range(k,n):
            sum=sum+nums[j]-nums[j-k]
            res=max(sum,res)
        return res/k



s=Solution()
arr=[1,12,-5,-6,50,3]
k=4
print(s.findMaxAverage(arr,k))
