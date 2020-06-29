#https://leetcode.com/problems/verifying-an-alien-dictionary/
class Solution(object):
    def isAlienSorted(self, words, order):
        char="abcdefghijklmnopqrstuvwxyz"
        res=[]
        dic={}
        #myDict=dict(zip(list(order),list(char)))
        for i in range(len(order)):
            dic[order[i]] = char[i]
        for word in words:
            temp=""
            for c in word:
                temp+=dic[c]
            #temp = ''.join([myDict[c] for c in word])
            res.append(temp)
        print(res)
        return res==sorted(res)

s=Solution()
#words = ["hello","leetcode"]
#order = "hlabcdefgijkmnopqrstuvwxyz"
words = ["word","world","row"]; order = "worldabcefghijkmnpqstuvxyz"
#words=["kuvp","q"];order="ngxlkthsjuoqcpavbfdermiywz"
print(s.isAlienSorted(words,order))

