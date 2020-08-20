#random paragraph
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
                if c.strip()=='%':
                    cnt+=1
                    res[cnt]=s
                    s=""
                else:
                    s+=c
            #print(res)
        res_len=len(res)
        r=random.randint(1,res_len)
        print("random Number:",r)
        print(res)
        return res[r]


s=Solution()
fl="/tmp/par.txt"
#for _ in range(10):
print(s.paragraph(fl))

"""
Print random paragraph

Sample data:
Hello
World
%
AAA
%
BBB
BBB
BBB
%
%
ABCD
%
"""
