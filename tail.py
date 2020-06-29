#Starting with small steps
import os
import time
#import platform
class Solution(object):
    def tail(self,fl,r):
        r.seek(0,os.SEEK_END)
        stat_old = os.stat(fl)
        stat_old_mtime = stat_old.st_mtime
        while True:
            line=r.readline()
            stat = os.stat(fl)
            stat_mtime = stat.st_mtime
            if stat_mtime<=stat_old_mtime:
                time.sleep(0.1)
                continue
            stat_old_mtime=stat_mtime
            yield line
        
        #print(stat)
        #return stat.st_mtime

s=Solution()
fl="/Users/malaybiswal/Downloads/misc.txt"
with open(fl,'r') as r:
    loglines = s.tail(fl,r)
    for line in loglines:
        print(line)

#print(s.tail(fl))
