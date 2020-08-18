import os
class Solution(object):
    def tail(self,fname,n):
        chunksize=4096
        remaining=0
        cur_pos=0
        i=0
        s=""
        with open(fname,'r') as r:

            r.seek(0,os.SEEK_END)
            remaining=r.tell()
            cur_pos=r.tell()-chunksize
            if cur_pos<=0:
                chunksize=remaining
                cur_pos=remaining
                r.seek(0,0)
                chunk=r.read(chunksize)
                chunks=chunk.splitlines()
                for j in range(len(chunks)-1,len(chunks)-n-1,-1):
                    s=chunks[j]+'\n'+s
                return s.strip()

                

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
                
                if cur_pos-len(chunk)>0:
                    cur_pos=cur_pos-len(chunk)
                    r.seek(remaining-(chunksize),0)
                elif cur_pos-len(chunk)<=0:
                    r.seek(0,0)
                    overflow=cur_pos-len(chunk)# extra going negative crossing 0 seek
                    chunk=r.read(chunksize+overflow)
                    s=chunk+s
                    break
                    #cur_pos=cur_pos-len(chunk)
        
            
        return s
            
s=Solution()
fl=input("Enter File Name:")
n=input("Enter tail count:")
n=int(n)
print(s.tail(fl,n))
