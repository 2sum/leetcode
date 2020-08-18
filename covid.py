# Asked oin Citrix interview 
# Given an array how many timnes it takes to spread covid to everyone.
#'X' is covid and they can transmit to only left,right,up,down (not diagonally). How many iteration it'll take to get everyone infected
class Solution(object):
    def covid(self, grid):
        row=len(grid)
        col=len(grid[0])
        temp=[['-' for x1 in range(col)]for x2 in range(row)]
        #print(row,col)
        flag=True
        print(temp)
        count=0
        res=0
        print(row,col)
        while flag:
            count=0
            res+=1
            for i in range(row):
                for j in range(col):
                    if(grid[i][j]=='X'):
                        temp[i][j]='X'
                        if i>=1:
                            temp[i-1][j]='X'
                        if  i<row-1:
                            temp[i+1][j]='X'
                        if  j>=1:
                            temp[i][j-1]='X'
                        if j<col-1:
                            temp[i][j+1]='X'
            print("TEMP:",temp)

            for x in range(len(temp)):
                for y in range(len(temp[0])):
                    if temp[x][y]=='X':
                        #print("x",x,"y",y)
                        grid[x][y]='X'
                        count+=1
            #print("COUNT:",count)
            if count==row*col:
                flag=False
        print(temp)
        return res
    


s=Solution()
#grid=[['-','-','-','-','-','-'],['X','-','-','-','-','-'],['-','-','-','-','-','-'],['-','-','X','-','-','-'],['-','-','-','-','-','-']]

grid=[['-','-','X','-'],['X','-','-','-'],['-','-','X','-']]
print(s.covid(grid))

