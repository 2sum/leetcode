#https://leetcode.com/problems/palindromic-substrings/
class Solution(object):
    def countSubstrings(self, s):
        n=len(s)
        count=0
        dp=[[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i]=1
            count+=1
        for i in range(n-1):
            if s[i]==s[i+1]:
                dp[i][i+1]=1
                count+=1
        k=3
        while k<=n:
            i=0
            while i<n-k+1:
                j=i+k-1
                if dp[i+1][j-1] and s[i]==s[j]:
                    dp[i][j]=1
                    count+=1
                i+=1
            k+=1
        print(dp)
        return count


s=Solution()
st="abad"
print(s.countSubstrings(st))
