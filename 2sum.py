class Solution(object):
    def twoSum(self, nums, target):
        """n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return[0,0]"""
        n=len(nums)
        dic={}
        for i in range(n):
            comp=target-nums[i]
            #dic[nums[i]]=i
            if comp in dic:
                return [dic[comp],i]
            dic[nums[i]]=i


s=Solution()
nums=[2, 7, 11, 15]
target=9
print(s.twoSum(nums,target))
