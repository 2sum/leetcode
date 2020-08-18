import math
from collections import OrderedDict
class Solution(object):
     def find(self):
         dic={}
         res_dic={}
         with open('dataset1.csv','r') as r:
             for lines in r.readlines():
                 ls = lines.split(',')
                 
                 dic[ls[0]]=ls[1]
         #print(dic)


         with open('dataset2.csv', 'r') as reader:
             for line in reader.readlines():
                 l=line.split(',')
                 
                 if(l[2].strip()=='bipedal'):
                     try:
                        
                        speed = ((float(l[1])/float(dic[l[0]]))-1)*(math.sqrt(float(dic[l[0]])*9.8))
                        res_dic[l[0]]=speed
                     except:
                         #print("ERROR for l[0] - row not found in dataset1.csv")
                         continue
         
         d_desc = OrderedDict(sorted(res_dic.items(),key=lambda kv:kv[1], reverse=True))
         
         for k,v in d_desc.items():
            print(k,v)
        
s=Solution()
s.find()
