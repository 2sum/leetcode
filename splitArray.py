#https://www.geeksforgeeks.org/split-array-two-equal-sum-subarrays/
class Solution(object):
    def splitarray(self,arr):
        sum=0
        left=0
        l=len(arr)
        
        for i in range(len(arr)):
            sum+=arr[i]
        right=sum
        for i in range(len(arr)):
            left+=arr[i]
            right=right-arr[i]
            print(left,right)
            if left==right:
                return [arr[0:i+1],arr[i+1:l+1]]
        return -1
s=Solution()
#a=[1 , 2 , 3 , 4 , 5 , 5]
#a=[4,1,2,3]
a=[4,3,2,1]
print(s.splitarray(a))
