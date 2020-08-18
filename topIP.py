''' AWS SysDev onsite coding
Write some code to parse an apache log file, 
grouping requests by /24 subnet and month and then give me the top 10 subnets from each month'''
class Solution(object):
    def find(self,ip):
        subnet=""
        dic={}
        count=0
        mnth=""
        lst=[]
        temp=[]
        x=0
        res=""
        with open (ip,"r") as fp:
            while(True):
                x+=1
                f=fp.readline()
                if not f:
                    for k,v in dic.items():
                        v=sorted(v,key=lambda x:x[1],reverse=True)
                        dic[k]=v
                    for k,v in dic.items():
                        res+=k+" Month has top subnets "+str(v)+"\n"
                    return res.strip()
                    
                line = f.split()
                s=line[0].split('.')
                subnet=s[0]+'.'+s[1]+'.'+s[2]
                m=line[3].split('/')
                mnth=m[1]
                if mnth not in dic:
                    temp.append([subnet,1])
                    dic[mnth]=temp
                    temp=[]
                else:
                    data=dic[mnth]
                    for i in range(len(data)):
                        if data[i][0]==subnet:
                            data[i][1]+=1
                            dic[mnth]=data
                            break
                        else:
                            if i==len(data)-1:
                                data.append([subnet,1])
                                dic[mnth]=data
s=Solution()
print(s.find("ip.csv"))
