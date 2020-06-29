#given string that contains different kind of parentheses, remove the invalid ones and return 
# new valid string (if multiple exists, return any). any types of parentheses, brackets and so on (),[],<>,{} . 
# Sample input: b(d)ss{}s}a -> b(d)ss{}sa for example
#https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
import re
class Solution(object):
    def parenthesis(self,par):
        stack = []
        ind_to_remove = set()
        ind=0
        for i,c in enumerate(par):
            if c not in "(){}[]":
                continue
            if c=="(" or c=="[" or c=="{":
                stack.append(i)
            elif not stack:
                ind_to_remove.add(i)
            else:
                stack.pop()
        print(stack,ind_to_remove)
        ind_to_remove = ind_to_remove.union(set(stack))
        res=[]
        for i,c in enumerate(par):
            if i not in ind_to_remove:
                res.append(c)
        return "".join(res)


            
                    
s=Solution()
strng="b(d)ss{}s}a"
#strng="(a(b(c)d)"
#strng=")("
print(s.parenthesis(strng))
