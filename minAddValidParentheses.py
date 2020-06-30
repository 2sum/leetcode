#https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
class Solution(object):
    def minAddToMakeValid(self, S):
        res=[]
        count=0
        for c in S:
            if c=="(":
                res.append(c)
            if c==")":#
                if len(res)>0:
                    res.pop()
                else:
                    count+=1
        return count+len(res)


s=Solution()
arr="()))(("
#arr="(()"
print(s.minAddToMakeValid(arr))
