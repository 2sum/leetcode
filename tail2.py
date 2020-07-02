# this works for tail -10, but not for tail -f where file is refreshed
import sys
import os
class Solution(object):
    def tail(self,n,fname):
        bufsize=4096
        fsize = os.stat(fname).st_size
        print("FILE SIZE:",fsize)
        iter=0
        with open(fname,'r') as f:
            if bufsize>fsize:
                bufsize=fsize-1
            data = []
            while True:
                iter+=1
                f.seek((fsize-bufsize)*iter)
                #data.extend(f.readlines())
                data+=f.readlines()
                if len(data) >= n or f.tell()==0:
                    return "".join(data[-n:])
                    #return data
                    break
s = Solution()
n=10
fl="/Users/malaybiswal/Downloads/a.txt"
print(s.tail(n,fl))


