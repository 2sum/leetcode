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
            line=""
            #print("where am i:",r.tell())
            line=r.readline()
            r.seek(0,os.SEEK_END)
            stat = os.stat(fl)
            stat_mtime = stat.st_mtime
            if stat_mtime<=stat_old_mtime:
                time.sleep(1)
                prev_seek=r.tell()
                continue
            else:
                line=""
                r.seek(0,os.SEEK_END)
                end=r.tell()
                r.seek(prev_seek,0)
                while r.tell()<end:
                    #print("TIMES:",stat_old_mtime,stat_mtime)
                    line+=r.readline()
                    #line.rstrip()
                    #line.lstrip()
                    #print("where am i after seek:",r.tell())
                r.seek(0,os.SEEK_END)
                stat_old_mtime=stat_mtime
                prev_seek=r.tell()
                yield line.strip()
        
        #print(stat)
        #return stat.st_mtime

s=Solution()
fl="/tmp/a.txt"
with open(fl,'r') as r:
    loglines = s.tail(fl,r)
    for line in loglines:
        print(line.strip())

#print(s.tail(fl))
