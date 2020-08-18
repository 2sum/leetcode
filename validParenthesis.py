class Solution(object):
    def isvalid(self,par):
        d={"}":"{",")":"(","]":"["}
        res=[]
        for c in par:
            if c in d.values():
                res.append(c)
            elif c in d.keys():
                if(len(res)==0):
                    return False
                if d[c]==res[-1]:
                    res.pop()
        if len(res)==0:
            return True
        else:
            return False

s=Solution()
par="()[]{}{([])}"
print(s.isvalid(par))
