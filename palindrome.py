#https://leetcode.com/problems/valid-palindrome/
class Solution(object):
    def isPalindrome(self, s):
        i=0
        j=len(s)-1
        while i<j:
            while i<j and not s[i].isalpha():
                i+=1
            while i<j and not s[j].isalpha():
                j-=1
            if i<j and s[i].lower()!=s[j].lower():
                return False
            i+=1
            j-=1
        return True
            

s=Solution()
strng="race a car"
#strng="A man, a plan, a canal: Panama"
print(s.isPalindrome(strng))
