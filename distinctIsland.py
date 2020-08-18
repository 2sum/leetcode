class Solution(object):
    def numDistinctIslands(self, grid):
        res=set()
        if not grid:
            return len(res)
        for i in range(len(grid)):
            for j  in range(len(grid[0])):
                if grid[i][j]==1:
                    self.cur=[]
                    self.dfs(i,j,i,j,grid)
                    tmp_island=str(self.cur)
                    if len(self.cur)>0 and tmp_island not in res:
                        res.add(tmp_island)
        return len(res)
    def dfs(self,i_0,j_0,i,j,grid):
        if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]!=1:
            return
        grid[i][j]=2
        self.cur.append([i-i_0,j-j_0])  
        self.dfs(i_0,j_0,i-1,j,grid)
        self.dfs(i_0,j_0,i+1,j,grid)
        self.dfs(i_0,j_0,i,j-1,grid)
        self.dfs(i_0,j_0,i,j+1,grid)

s=Solution()
arr=[[0,1]]
#arr=[[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
#arr=[[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
print(s.numDistinctIslands(arr))
