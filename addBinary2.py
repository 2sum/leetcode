class Solution(object):
    def addBinary(self,a,b):
        if len(a)>len(b):
            b='0'*(len(a)-len(b))+b
        if len(b)>len(a):
            a='0'*(len(b)-len(a))+a
        carry=0
        #res=[]
        res=""
        for i in range(len(a)-1,-1,-1):
            if a[i]=='1':
                carry+=1
            if b[i]=='1':
                carry+=1
            if carry%2==1:
                #res.append('1')
                res='1'+res
            else:
                #res.append('0')
                res='0'+res
            carry//=2
        if carry==1:
            #res.append('1')
            res='1'+res
        #res.reverse()
        #return ''.join(res)
        return res

s=Solution()
a="1"
b="0"
print(s.addBinary(a,b))
