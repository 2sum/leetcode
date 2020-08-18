#given string that contains different kind of parentheses, remove the invalid ones and return 
# new valid string (if multiple exists, return any). any types of parentheses, brackets and so on (),[],<>,{} . 
# Sample input: b(d)ss{}s}a -> b(d)ss{}sa for example
#https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
import re
class Solution(object):
    def parenthesis(self,par):
        stack = []
        ind_to_remove = set()
        dic={"}":"{",")":"(","]":"["}
        ind=0
        for i,c in enumerate(par):
            if c not in "(){}[]":
                print("IN first if:",i,c)
                continue
            if c in dic.values():
                stack.append(i)
                print("IN 2nd if:",i,c)
            elif not stack:
                ind_to_remove.add(i)
                print("IN ELif remove IND:",i,c)
            else:
                print("IN ELSE POP:",i,c,stack)
                if par[stack[-1]]==dic[c]:
                    print("      popping:",stack)
                    stack.pop()
                    print("      After popping:",stack)
                else:
                    ind_to_remove.add(i)
                    print("   IND_TO_REMOVE:",ind_to_remove)
                
        print(stack,ind_to_remove)
        ind_to_remove = ind_to_remove.union(set(stack))
        res=[]
        print(stack,ind_to_remove)
        for i,c in enumerate(par):
            if i not in ind_to_remove:
                res.append(c)
        return "".join(res)
                    
s=Solution()
#strng = "[b(d)s}a"
strng="b(d)ss{}s}a"
#strng="(a(b(c)d)"
#strng=")("
print("RESULT:",s.parenthesis(strng))
