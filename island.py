class Solution(object):
    def numIslands(self, grid):
        row=len(grid)
        col=len(grid[0])
        #print(row,col)
        count=0
        for i in range(row):
            #print("--------------")
            for j in range(col):
                if(grid[i][j]==1):
                    self.dfs(grid,i,j)
                    count+=1
        return count
    def dfs(self,grid,i,j):
        if(i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]!=1):
            return
        grid[i][j]=0
        self.dfs(grid,i+1,j)
        self.dfs(grid,i-1,j)
        self.dfs(grid,i,j+1)
        self.dfs(grid,i,j-1)  


s=Solution()
grid=[[1,1,0,0,0],[1,1,0,0,0],[0,0,1,0,0],[0,0,0,1,1]]
print(s.numIslands(grid))
#11000
#11000
#00100
#00011
