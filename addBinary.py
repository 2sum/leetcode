class Solution(object):
    def addBinary(self, a, b):
        
        if len(b)>len(a):
            a='0'*(len(b)-len(a))+a
        if len(a)>len(b):
            b='0'*(len(a)-len(b))+b
        carry=0
        temp=0
        res=''
        print(a,b)
        for i in range(len(a)-1,-1,-1):
            temp=int(a[i])+int(b[i])+carry
            if temp<2:
                carry=0
            elif temp>=2:
                carry=1
                temp-=2
            res=str(temp)+res
            print(res)
        if carry==0:
            return res
        else:
            return ('1'+res)

s=Solution()
a="11"
b="1"
print(s.addBinary(a,b))
