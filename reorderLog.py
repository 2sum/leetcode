#https://leetcode.com/problems/reorder-data-in-log-files/
class Solution(object):
    def reorderLogFiles(self, logs):
        letter={}
        digit=[]
        for log in logs:
            ind=log.index(" ")
            s=log.split()
            if s[1].isdigit():
                digit.append(log)
            else:
                letter[log]=log[ind:]
        print("LETTER DICT:",letter)
        sorted_letter=sorted(letter,key=lambda x:(letter[x],x))#THis is sorting first by value and if same value then by key
        #sorted_letter=sorted(letter,key=lambda x:x[0])
        print("SORT AFTER LETTER DICT:",sorted_letter) 
        return sorted_letter+digit


s=Solution()
logs=["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]
#logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
print(s.reorderLogFiles(logs))
