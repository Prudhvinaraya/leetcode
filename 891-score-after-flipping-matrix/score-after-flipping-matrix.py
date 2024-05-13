class Solution:
    def matrixScore(self,grid):
        m, n = len(grid), len(grid[0])

        # Step 1: Toggle rows to make sure the most significant bit of each row is 1
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] = 1 - grid[i][j]

        # Step 2: Toggle columns to maximize each column's contribution to the total score
        score = 0
        for j in range(n):
            count_of_ones = sum(grid[i][j] for i in range(m))
            score += max(count_of_ones, m - count_of_ones) * (1 << (n - 1 - j))

        return score
