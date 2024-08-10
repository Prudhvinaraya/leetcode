class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        rows1, cols1 = len(grid), len(grid[0])
        rows2, cols2 = rows1 * 3, cols1 * 3
        grid2 = [[0]*cols2 for _ in range(rows2)]

        for r in range(rows1) :
            for c in range(cols1) :
                r2, c2 = r*3, c*3
                if grid[r][c] == "/" :
                    grid2[r2][c2+2] = 1
                    grid2[r2+1][c2+1] = 1
                    grid2[r2+2][c2] = 1
                elif grid[r][c] == "\\" :
                    grid2[r2][c2] = 1
                    grid2[r2+1][c2+1] = 1
                    grid2[r2+2][c2+2] = 1

        def dfs(r, c, visit) : 
            if (r < 0 or r >= rows2 or c < 0 or c >= cols2 or (r, c) in visit or grid2[r][c] != 0):
                return

            visit.add((r, c))
            dfs(r+1, c, visit)
            dfs(r-1, c, visit)
            dfs(r, c+1, visit)
            dfs(r, c-1, visit)


        visit = set()
        res = 0

        for r in range(rows2):
            for c in range(cols2) :
                if (r, c) not in visit and grid2[r][c] == 0:
                    dfs(r, c, visit)
                    res += 1
        return res