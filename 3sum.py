class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        res=[]
        if not nums:
            return res
        if nums[0]>0:
            return res
        for i in range(0,len(nums)-2):
            l=i+1
            r=len(nums)-1
            if(nums[i]>0):
                    break
            if i>0 and nums[i]==nums[i-1]:
                continue
            while(l<r):
                
                if(nums[i]+nums[l]+nums[r]==0):
                    res.append([nums[i],nums[l],nums[r]])
                    if   nums[l]==nums[l+1]:
                        l+=1
                    elif   nums[r]==nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
                if(nums[i]+nums[l]+nums[r])<0:
                    l+=1
                elif nums[i]+nums[l]+nums[r]>0:
                    r-=1
        return res

s=Solution()
nums=[-1,0,1,2,-1,-4]
#nums=[-1,0,1]
#nums=[-1, 0, 1, 2, -1, -4]
print(s.threeSum(nums))
