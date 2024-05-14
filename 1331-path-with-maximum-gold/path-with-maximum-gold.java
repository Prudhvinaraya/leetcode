class Solution {

    private final List<Integer> dx = Arrays.asList(-1, 0, 0, 1);
    private final List<Integer> dy = Arrays.asList(0, -1, 1, 0);

    public int dfs(int i, int j, int[][] grid) {
        int n = grid.length;
        int m = grid[0].length;

        if (i < 0 || i >= n || j >= m || j < 0 || grid[i][j] == 0)
            return 0;

        int maxSum = 0;
        int curVal = grid[i][j];

        for (int d = 0; d < 4; d++) {
            int ni = i + dx.get(d);
            int nj = j + dy.get(d);
            grid[i][j] = 0;
            maxSum = Math.max(maxSum, curVal + dfs(ni, nj, grid));
            grid[i][j] = curVal;
        }

        return maxSum;
    }

    public int getMaximumGold(int[][] grid) {
        int n = grid.length;
        int m = grid[0].length;

        int ans = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] != 0)
                    ans = Math.max(ans, dfs(i, j, grid));
            }
        }
        return ans;
    }
}