import random
class Solution(object):
    def paragraph(self,fl):
        cnt=0
        res={}
        c=" "
        s=""
        with open (fl,'r') as f:
            while(c):
                
                c=f.readline()
                if '%' in c:
                    cnt+=1
                    res[cnt]=s
                    s=""
                elif '%' not in c:
                    s+=c
        res_len=len(res)
        r=random.randint(1,res_len)
        return res[r]


s=Solution()
fl="par.txt"
print(s.paragraph(fl))