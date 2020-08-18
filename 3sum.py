class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        n=len(nums)
        res=set()
        if n==0:
            return res
        if nums[0]>0:
            return res
        for i in range(n-2):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=n-1

            while(l<r):
                if nums[i]+nums[l]+nums[r]==0:
                    res.add((nums[i],nums[l],nums[r]))
                    if nums[l]==nums[l+1]:
                        l+=1
                    if nums[r]==nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
                elif nums[i]+nums[l]+nums[r]<0:
                    l+=1
                else:
                    r-=1
        return res



s=Solution()
nums=[-1,0,1,2,-1,-4]
#nums=[-1,0,1]
#nums=[-1, 0, 1, 2, -1, -4]
print(s.threeSum(nums))
