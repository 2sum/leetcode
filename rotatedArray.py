class Solution(object):
    def search(self, nums, target):
        n=len(nums)
        left=0;right=n-1
        l=self.findRotateIndex(left,right)
        print(l)
        if nums[l]==target:
            return l
        if l==0:
            return self.findTarget(0,n-1)
        if target < nums[0]:
            return self.findTarget(l,n-1)
        return self.findTarget(0,l)
        #m=self.findTarget(l,left,right)
        #return m
    def findRotateIndex(self,left,right):
        if nums[left]<nums[right]:
                return 0
        while(left<=right):
            pivot=(left+right)//2
            print("****",nums[pivot],nums[pivot-1],pivot)
            if nums[pivot]>nums[pivot+1]:
                return pivot+1
            else:
                if nums[pivot]<nums[right]:
                    right=pivot-1
                else:
                    left=pivot+1
    def findTarget(self,left,right):
        
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            else:
                if(nums[mid]<target):
                    left=mid+1
                else:
                    right=mid-1
        return -1

s=Solution()
nums = [4,5,6,7,0,1,2]; target = 0
#nums=[10,12,14,18,22,23,24,25,26,27,28,5,6,7,8,9];target = 9
print(s.search(nums,target))
