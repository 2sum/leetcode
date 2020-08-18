#https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60
#https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/discuss/468840/Python-3-O(N)-No-collections-solution
class Solution(object):
    def numPairsDivisibleBy60(self,time):
        res=0
        dic={}
        for t in time:
            temp=t%60
            if 60-temp in dic:
                res+=dic[60-temp]
            if temp not in dic:
                dic[temp]=1
            else:
                if temp==0:
                    res+=dic[0]
                dic[temp]+=1
        return res
s=Solution()
time=[10,30,100,20,40,50]
print(s.numPairsDivisibleBy60(time))
