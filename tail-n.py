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
            print(r.tell(),cur_pos)
            r.seek(cur_pos,0)
            while  n>0:
                print("-------------------")
                i+=1
                chunk = r.read(chunksize)
                n -= chunk.count(os.linesep)
                if n==0:
                    chunks=chunk.splitlines()
                    l=len(chunks)
                    chunk=chunks[-1]
                print("n:",n)
                s=chunk+s
                print(s,i)
                remaining -= len(chunk)
                r.seek(remaining-(chunksize),0)
                cur_pos=cur_pos-len(chunk)
        
            
        print("====================OUTPUT================")
        return s
            


s=Solution()
fl="/Users/malaybiswal/Downloads/a.txt"
n=3

print(s.tail(fl,n))
#with open(fl,'r') as r:
    #loglines = s.tail(fl,n)
    #for line in loglines:
    #   print(line.strip())
