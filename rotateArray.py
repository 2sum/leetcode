#https://leetcode.com/problems/rotate-array/

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #print(nums,k)
        l=len(nums)
        if len(nums)<=1:
            return nums
        if k>l:
            k=mod(k,l)
        if k==l:
            return nums
       
        arr1=nums[l-k:l+1]
        print(arr1)
        for i in range(l-k-1,-1,-1):
            nums[l-1]=nums[i]
            l=l-1
        if(k>=1):
            for j in range(0,k,1):
                nums[j]=arr1[j]
        print(nums)
        return nums
s=Solution()
arr=[1,2,3,4,5,7]
k=3
print(s.rotate(arr,k))
