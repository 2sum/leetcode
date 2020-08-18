#https://leetcode.com/problems/subsets/
class Solution(object):
    def subsets(self,num):
        res=[[]]
        for n in num:
            for i in res:
                res=res+[i+[n]]
        return res
s=Solution()
num=[1,2,3]
print(s.subsets(num))
