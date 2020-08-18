#Return all subarrays of array FaceBook question
from itertools import combinations 
class Solution(object):
     
    '''def get(self,arr):
        def printSubArrays(arr, start, end): 
            
    # Stop if we have reached the end of the array     
            if end == len(arr): 
                return res
      
    # Increment the end point and start from 0 
            elif start > end: 
                return printSubArrays(arr, 0, end + 1) 
          
    # Print the subarray and increment the starting 
    # point 
            else: 
                print(arr[start:end + 1]) 
                res.append(arr[start:end + 1])
                return printSubArrays(arr, start + 1, end)
        start=0
        res=[]
        end=0
        res=printSubArrays(arr,start,end)
        return res'''
    '''def get(self,nums):
        res=[[]]
        curr=[]
        n=0
        def helper(nums, curr, n):
            if n==len(nums):
                res.append(curr)
                return
            
            helper(nums, curr+[nums[n]], n+1)
            helper(nums, curr, n+1)
        helper(nums, curr, n)
        if len(nums)==0:
            return []
        else:
            return res[1:]'''

    '''def get(self,nums):
        n = len(nums)
        subset=[]
        for i in range(n+1):
            sub=list(combinations(nums,i))
            print(i,sub)
            for s in sub:
                subset.append(s)
        return subset'''
        
    def get(self,nums):
        res=[[]]
        for num in nums:
            for curr in res:
                res=res+[curr+[num]]
        return res
    
            
        

s=Solution()
arr=[1,2,3]
print("RES:",s.get(arr))
