import java.util.Stack;

class Solution {
    public boolean exist(char[][] board, String word) {
        int m = board.length;
        int n = board[0].length;
        
        // Convert the word into an array of characters
        char[] arr = word.toCharArray();
        
        // Define a stack to store characters of the word
        Stack<Character> stk = new Stack<>();
        
        // Push characters onto the stack in reverse order
        for (int i = arr.length - 1; i >= 0; i--) {
            stk.push(arr[i]);
        }
        
        // Iterate through the board and start DFS from each cell
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (dfs(i, j, cloneStack(stk), board)) { // Pass a copy of the stack
                    return true;
                }
            }
        }
        
        return false;
    }
    
    // Depth-first search (DFS) function to traverse the board
    private boolean dfs(int row, int col, Stack<Character> stk, char[][] board) {
        int m = board.length;
        int n = board[0].length;
        
        // Base case: If the stack is empty, all characters in the word have been matched
        if (stk.isEmpty()) {
            return true;
        }

        // If current position is out of bounds or doesn't match the top of the stack
        if (row < 0 || row >= m || col < 0 || col >= n || board[row][col] != stk.peek()) {
            return false;
        }

        char temp = board[row][col];
        board[row][col] = '#'; // Mark cell as visited

        stk.pop(); // Matched character, pop from stack

        // Explore neighbors
        if (dfs(row + 1, col, stk, board) || dfs(row - 1, col, stk, board) ||
            dfs(row, col + 1, stk, board) || dfs(row, col - 1, stk, board)) {
            return true;
        }

        board[row][col] = temp; // Revert cell to original value
        stk.push(temp); // Restore popped character
        return false;
    }
    
    // Function to clone the stack
    private Stack<Character> cloneStack(Stack<Character> stk) {
        Stack<Character> clone = new Stack<>();
        clone.addAll(stk);
        return clone;
    }
}
