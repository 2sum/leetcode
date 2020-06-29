class Solution(object):
    def convert(self,roman):
        res=0
        cnt=0
        temp=0
        dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for c in range(len(roman)-1,-1,-1):
            cnt+=1
            if cnt<=1:
                i=dic[roman[c]]
                res=i
                temp=i
            else:
                
                if dic[roman[c]]<temp:
                    res=res-dic[roman[c]]
                else:
                    res=res+dic[roman[c]]
                temp=dic[roman[c]]
            print(res)
        return res


s=Solution()
#r='VI'
r='MCMXCIV'
print(s.convert(r))
