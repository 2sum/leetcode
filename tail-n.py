import os
class Solution(object):
    def tail(self,fname,n):
        chunksize=4
        remaining=0
        cur_pos=0
        i=0
        s=""
        with open(fname,'r') as r:

            r.seek(0,os.SEEK_END)
            remaining=r.tell()
            cur_pos=r.tell()-chunksize
            r.seek(cur_pos,0)
            while  n>0:
                i+=1
                chunk = r.read(chunksize)
                n -= chunk.count(os.linesep)
                if n==0:
                    chunks=chunk.splitlines()
                    l=len(chunks)
                    chunk=chunks[-1]
                s=chunk+s
                remaining -= len(chunk)
                r.seek(remaining-(chunksize),0)
                cur_pos=cur_pos-len(chunk)
        return s
s=Solution()
fl=input("Enter File Name:")
n=input("Enter tail count:")
n=int(n)
print(s.tail(fl,n))
