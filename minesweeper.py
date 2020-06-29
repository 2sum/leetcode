class Solution(object):
    def updateBoard(self, board, click):
        if board[click[0]][click[1]]=='M':
            board[click[0]][click[1]]='X'
            return board
        else:
            self.dfs(board,click)
        return board
    def recfind(self,board,click):
        count=0
        neighbors=[[click[0]-1,click[1]],[click[0]-1,click[1]-1],[click[0]-1,click[1]+1],[click[0]+1,click[1]],[click[0]+1,click[1]+1],[click[0]+1,click[1]-1],[click[0],click[1]-1],[click[0],click[1]+1]]
        for n in neighbors:
            if n[0] < 0 or n[0]>=len(board) or  n[1]<0 or n[1]>=len(board[0]):
                continue
            elif board[n[0]][n[1]]=='M':
                count+=1
        return count>0,count  
    def dfs(self,board,click):
        if click[0]<0 or click[0]>=len(board) or click[1]<0 or click[1]>=len(board[0]):
            return
        else:
            ismine,minecount = self.recfind(board,click)
            if board[click[0]][click[1]]=='E' and ismine is True:
                board[click[0]][click[1]]=str(minecount)
            elif board[click[0]][click[1]]=='E' and ismine is False:
                board[click[0]][click[1]]='B'
                self.dfs(board,[click[0]-1,click[1]])
                self.dfs(board,[click[0]-1,click[1]-1])
                self.dfs(board,[click[0]-1,click[1]+1])
                self.dfs(board,[click[0]+1,click[1]])
                self.dfs(board,[click[0]+1,click[1]-1])
                self.dfs(board,[click[0]+1,click[1]+1])
                self.dfs(board,[click[0],click[1]+1])
                self.dfs(board,[click[0],click[1]-1])



s = Solution()
board=[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]
click = [3,0]
print(s.updateBoard(board,click))
