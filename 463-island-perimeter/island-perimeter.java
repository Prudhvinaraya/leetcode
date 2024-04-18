public class Solution {
    public int islandPerimeter(int[][] grid) {
        int perimeter = 0;
        int rows = grid.length;
        int cols = grid[0].length;
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == 1) {
                    perimeter += 4;  // Assuming all sides are initially counted
                    if (i > 0 && grid[i - 1][j] == 1) {
                        perimeter -= 2;  // Subtract if neighboring cell to the top is also land
                    }
                    if (j > 0 && grid[i][j - 1] == 1) {
                        perimeter -= 2;  // Subtract if neighboring cell to the left is also land
                    }
                }
            }
        }
        
        return perimeter;
    }
}

