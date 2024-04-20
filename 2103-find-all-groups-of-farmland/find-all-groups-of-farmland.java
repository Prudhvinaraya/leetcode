import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[][] findFarmland(int[][] land) {
        List<int[]> groups = new ArrayList<>();
        int m = land.length;
        int n = land[0].length;
        boolean[][] visited = new boolean[m][n];
        int[][] directions = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (land[r][c] == 1 && !visited[r][c]) {
                    int[] topLeft = {r, c};
                    int[] bottomRight = {r, c};
                    dfs(land, visited, r, c, topLeft, bottomRight, directions);
                    groups.add(new int[]{topLeft[0], topLeft[1], bottomRight[0], bottomRight[1]});
                }
            }
        }

        return groups.toArray(new int[groups.size()][]);
    }

    private void dfs(int[][] land, boolean[][] visited, int r, int c, int[] topLeft, int[] bottomRight, int[][] directions) {
        int m = land.length;
        int n = land[0].length;

        visited[r][c] = true;
        bottomRight[0] = Math.max(bottomRight[0], r);
        bottomRight[1] = Math.max(bottomRight[1], c);

        for (int[] dir : directions) {
            int nr = r + dir[0];
            int nc = c + dir[1];
            if (nr >= 0 && nr < m && nc >= 0 && nc < n && land[nr][nc] == 1 && !visited[nr][nc]) {
                dfs(land, visited, nr, nc, topLeft, bottomRight, directions);
            }
        }
    }
}
