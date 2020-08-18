class Solution(object):
    def find(self,arr):
        sum=0
        n=len(arr)
        if n<2:
            return -1
       
        for i in range(len(arr)):
            sum+=arr[i]
        mid=sum/2
        print("MID:",mid)
        if sum%2!=0:
            return -1
        for i in range(len(arr)):
            sum-=arr[i]
            if sum==mid:
                return [arr[0:i+1],arr[i+1:n]]
        return -1   


s=Solution()
#arr=[-7,1,5,2,-4,3,0]
#arr=[1,2,3,5,1]
arr=[1,2,1,1,3]
#arr=[1]
print(s.find(arr))
