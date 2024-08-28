class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        visited = set()
        delta = [(0,-1),(0,1),(-1,0),(1,0)]
        ans = 0
        N , M = len(grid1) , len(grid1[0])
        def findIslands(startx,starty,arr):
            nonlocal visited
            queue = collections.deque()
            queue.append((startx,starty))
            visited.add((startx,starty))
            subIsland = True
            while len(queue):
                x,y = queue.popleft()
                if not grid1[x][y]:
                    subIsland = False
                for dx,dy in delta:
                    x1,y1 = x+dx , y+dy
                    if 0 <= x1 < N and 0 <= y1 < M and (x1,y1) not in visited and grid2[x1][y1]:
                        queue.append((x1,y1))
                        visited.add((x1,y1))
            
            return 1 if subIsland else 0
        
        for i in range(N):
            for j in range(M):
                if grid2[i][j] and (i,j) not in visited:
                    ans += findIslands(i,j,grid2)
        return ans