#https://leetcode.com/problems/subdomain-visit-count/
class Solution(object):
    def subdomainVisits(self, cpdomains):
        res={}
        temp=""
        for domains in cpdomains:
            domain=domains.split()
            d=domain[1].split('.')
            for i in range(len(d)-1,-1,-1):
                if temp!="":
                    temp=d[i]+'.'+temp
                if temp=="":
                    temp=d[i]+temp
                
                #print(temp,domain[0])
                if temp in res:
                    res[temp]+=int(domain[0])
                if temp not in res:
                    res[temp]=int(domain[0])
                
            #print(res)
            temp=""
        return res

s=Solution()
domains=["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
print(s.subdomainVisits(domains))
