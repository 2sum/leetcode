#Populate board with battleship of n grid and m length, for example a grid of 10X10 with 
#battleship of length 8
import random
class Solution(object):
     def createGrid(self,n,l):
         overflow=0
         grid = [[None for x in range(n)] for y in range(n)]
         r = random.randint(0,n)
         #r=0
         print("r:",r)
         if l>n:
             return -1
         if n<1:
             return grid
         
         print("r",r,"n:",n,"l:",l)
         if(r+l-1>=n):
             overflow=n-l
             r=overflow
         
         print("overflow:",overflow,"r",r)
         side = random.choice( ['horizontal', 'vertical'] )
         #side= 'horizontal'
         print(side,r)
         for i in range(n):
             for j in range(n):
                if(side=='vertical'):
                    if i >= r and i<r+l and j==r:
                        print("IF Vertival:",i,j)
                        grid[i][j]='X'
                    else:
                        #print("ELSE Vertival:",i,j)
                        grid[i][j]='.'
                else:
                    #print("i:",i,"j:",j,"maxgo:",maxgo,"r:",r)
                    if j >= r and j<r+l and i==r:
                        print("IF Hor:",i,j)
                        grid[i][j]='X'
                    else:
                        #print("ELSE Hor:",i,j)
                        grid[i][j]='.'
         #print("GRID:",grid)
         return grid




s=Solution()
array_len=7
battleship_len=3
print(s.createGrid(array_len,battleship_len))

