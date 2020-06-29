#https://leetcode.com/problems/friends-of-appropriate-ages/
class Solution(object):
    def find(self,ages):
        count = [0]*121
        for a in ages:
            count[a]+=1
        ans=0
        print(count)
        for ageA,countA in enumerate(count):
            for ageB,countB in enumerate(count):
                if ageA*0.5+7 >= ageB:
                    continue
                elif ageB > ageA:
                    continue
                elif ageB > 100 and ageA < 100:
                    continue
                ans += countA*countB
                if ageA == ageB:
                    ans-=countA
        return ans

s=Solution()
#ages=[20,30,100,110,120]
ages = [16,17,18]
print(s.find(ages))
