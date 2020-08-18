#https://en.wikipedia.org/wiki/Luhn_algorithm
class Solution(object):
    def calc(self,num):
        n=str(num)
        l=len(n)
        c=0
        res=0
        temp=0
        for i in range(l-1,-1,-1):
            c+=1
            if(c%2==0):
                temp=int(n[i])*2
                if temp>=10:
                    temp=temp-9
                #n[i]=temp
                #n=n[0:i]+str(temp)+n[i+2:l]
                res+=temp
                #print(n,c,n[i],i,"RES:",res,"TEMP:",temp)
                
            else:
                
                res+=int(n[i])
                #print("--",n,c,n[i],i,"RES:",res,"TEMP:",temp)
                continue
        res=res*9
        res=res%10
        if res == 0:
            return True
        else:
            return False


s=Solution()
num=79927398713
print("LUHN's Number is:",s.calc(num))


