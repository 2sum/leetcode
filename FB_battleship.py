"""[. X . .  
    . X . .
    . X . .
    . . . .]
 0,0 0,3
 1,1 1,2
 2,2
 3,3
 0,0 0,3 0,6 ...0,99
 3,0 3,"""

# 1 battleship of length 3  , horizontaly or vertically
# you are given findbomb()
# return bomb co-ordinates
"""res=[]
 for i in range(n):
    for j in range(n):
        if bomb(i,j):
            find(i,j)
            res.append([i,j])
            return res
 retun res

def find(i,j):
    if bomb(i,j+1):
        res.append([i,j+1])
        res.append([i,j+2])
       
    
    bomb(i+1,j)

return res"""

class Solution(object):
    def findCoordinate(self,board):
        print(board)
        count=0
        res=[]
        c=0
        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                c+=1
                if board[i][j]=='X':
                    self.dfs(board,i,j)
                    count+=1
                    res.append([i,j])
                    if count==3:
                        print("Traversed through :",c," Many Times to destroy")
                        return res
        return res
    def dfs(self,baord,i,j):
        if (i>0 or i<len(board) or j>0 or j<len(board[0]) or board[i][j]=='X'):
            return
        self.dfs(board,i-1,j)
        self.dfs(board,i+1,j)
        self.dfs(board,i,j-1)
        self.dfs(board,i,j+1)

s=Solution()
#board=[['.','.','.','.'],['.','X','.','.'],['.','X','.','.'],['.','X','.','.']]
board=[['.','X','.','.'],['.','X','.','.'],['.','X','.','.'],['.','.','.','.']]
print(s.findCoordinate(board))


"""Populate board with battleship of n grid and m length, for example a grid of 10X10 with 
battleship of length 8"""
