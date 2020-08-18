class Solution(object):
    def replace(self,fl):
        chunk=50
        email="abc@gmail.com"
        e=email.split('@')
        e1=len(e[0])
        e2=len(e[1])
        l=len(email)
        w = open("/Users/malaybiswal/malay_procore/python/leetcode/nobodyop.txt","w")
        cur_line=""
        i=0
        with open(fl,'r') as reader:
            while(True):
                i+=1
                line = reader.read(chunk)
                print(i,"Original chunk:",line)
                if not line:
                    break
                ln=len(line)
                
                if l>0:#substring for email check from beginning
                    first=line[:l]
                if ln>l:#susbtring for email check from end
                    last=line[ln-l:]#getting substring from end of chunk with size of email
                if '@' in last and last!=email:
                    ind=len(last)-last.rfind('@')+e1+1 
                    pos=reader.tell()
                    pos=pos-ind
                    p=chunk-ind
                    prev=line[:p]
                    prev=prev.replace(email,'nobody')
                    w.write(prev)
                    reader.seek(pos,0)#seek position back to start of partial email
                    line = reader.read(chunk)
                    
                if '@' in first and first!=email:
                    ind=first.find('@')
                    pos=reader.tell()-chunk-(e1-ind)
                    p=reader.tell()-chunk
                    nxt=line[p:]
                    nxt=nxt.replace(email,'nobody')
                    w.write(nxt)
                    reader.seek(pos,0)
                    line = reader.read(chunk)
                    
                line=line.replace(email,'nobody')
                print(i,"Modified One:",line)
                w.write(line)
            w.close()


s=Solution()
s.replace('/Users/malaybiswal/malay_procore/python/leetcode/nobody.txt')
