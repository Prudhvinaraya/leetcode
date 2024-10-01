class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int: 
        def dfs(i,j):
            #base case 1
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
                return 0
            #base case2
            if grid[i][j]==0:
                return 0
            gold=grid[i][j]
            grid[i][j]=0
            maxpath=max(dfs(i+1,j),dfs(i,j+1),dfs(i-1,j),dfs(i,j-1))
            grid[i][j]=gold
            return gold+maxpath
        return max(dfs(i,j) for i in range(len(grid)) for j in range(len(grid[0])))
        
                
                