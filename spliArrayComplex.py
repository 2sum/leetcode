#https://leetcode.com/problems/partition-equal-subset-sum/
class Solution(object):
    def cansplit(self,arr):
        arr.sort()
        print(arr)
        sum=0
        for i in range(len(arr)):
            sum+=arr[i]
        lsum=sum
        rsum=0
        for i in range(len(arr)-1,-1,-1):
            lsum=lsum-arr[i]
            rsum=rsum+arr[i]
            print(lsum,rsum,sum)
            if lsum==rsum:
                return True
            #if lsum>rsum:
            #    return False
        return False

s=Solution()
#a=[1,5,11,5,6]
a=[3,3,3,4,5]
a=[1,2,3,4,5,6,7]
print(s.cansplit(a))
