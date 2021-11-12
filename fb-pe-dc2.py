# We have multiple DataCenters (DCs) and we want to run a simulation (ahead of time)
# to ensure that when any ONE of them goes down, we can still run ALL our services.

# We have 2 rules:
# 1. Services don't share hosts - each instance takes full host.
# 2. Each service can run and be spread across hosts (of matching type) in any DC

# Write a program that will return:
# 0, if during failure of one DC we still have enough capacity for all services
# 1, if during failure of one DC we won't have enough capacity for all services.
# Also print what host types, and how many of them are missing in order to run our services

# You're given 2 datasets:
# 1. datacenters.csv - how many hosts of each type are in DCs
# 2. services.csv - how many hosts of what type are needed per service

# cat datacenters.csv
# NAME, HOST _TYPE, COUNT
# NORTH_AMERICA_01, COMPUTE_LOW, 800
# NORTH_AMERICA_01, COMPUTE_HIGH, 500
# NORTH_AMERICA_01, BIG_MEMORY, 500
# NORTH_AMERICA_02, COMPUTE_LOW, 200
# EUROPE_01, COMPUTE_HIGH, 500
# EUROPE_02, COMPUTE_HIGH, 500
# EUROPE_02, BIG_MEMORY, 600
# EUROPE_02, GPU, 800

# cat services.csv
# SERVICE, HOST-TYPE, COUNT
# test, COMPUTE_LOW, 100
# staging, COMPUTE_LOW, 400
# www, COMPUTE_HIGH, 1000
# api, BIG_MEMORY, 100

# In this example, if NORTH_AMERICA_01 goes down, we lose 800
# COMPUTE-LOW hosts, 500 COMPUTE_HIGH and 500 BIG_MEMORY
# We want to make sure that when this DC (or another random DC) is lost,
# with all hosts from it, we still have enough hosts globally to meet the
# requirements of all our services
class Solution:
    def capacity(self,dcname):
        i=0
        j=0
        res={}
        dc={}
        with open ('/Users/malaybiswal/malay_personal/python/LC/service.txt','r') as f1:
            lines=f1.readline()
            while(lines!=''):
                i+=1
                if i>1:
                    line=lines.split(',')
                    if line[1].strip() not in res:
                        res[line[1].strip()]=int(line[2].strip())
                    else:
                        temp=int(line[2].strip())
                        temp2=res[line[1].strip()]
                        res[line[1].strip()]=temp+temp2
                lines=f1.readline()
        print(res)
        with open ('/Users/malaybiswal/malay_personal/python/LC/dc.txt','r') as f2:
            lns=f2.readline()
            while(lns!=''):
                j+=1
                if j>1:
                    l=lns.split(',')
                    if l[0].strip()!=dcname:
                        if l[1].strip() in res:
                            cnt=int(l[2].strip())
                            cnt1=res[l[1].strip()]
                            print(l[0],l[1],cnt,cnt1)
                            res[l[1].strip()]=cnt1-cnt
                lns=f2.readline()
        print(res)
        for k,v in res.items():
            if v>0:
                print(k,' instance type quantity ',v, ' needed if ',dcname, ' DC is DOWN')
                return 1
            else:
                return 0

s=Solution()
#service='test'
dcname='NORTH_AMERICA_01'
print(s.capacity(dcname))