#https://leetcode.com/problems/degree-of-an-array/
class Solution(object):
    def findShortestSubArray(self,nums):
        dic={}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]]=[1,i,i]
            else:
                dic[nums[i]][0]+=1
                dic[nums[i]][2]=i
        print(dic)
        maxDegree=0
        for val in dic.values():
            if val[0]>maxDegree:
                maxDegree=val[0]
        mindiff=len(nums)
        print("MAXDEGREE:",maxDegree)
        for k,v in dic.items():
            if v[0]==maxDegree:
                diff=(v[2]-v[1])+1
                print(v[2],v[1])
                if diff<mindiff:
                    mindiff=diff
        return mindiff
        
        
s=Solution()
nums=[1,2,2,3,1]
#nums = [1,2,2,3,1,4,2]
print(s.findShortestSubArray(nums))
