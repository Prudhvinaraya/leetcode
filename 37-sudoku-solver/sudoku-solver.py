class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        self.solve(board)

    def find_empty(self, board):
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    return r, c  # Return the row and column of the empty cell
        return None  # If no empty cells are found, return None

    def is_valid(self, board, r, c, n):
        # Check the row and column
        for i in range(9):
            if board[r][i] == n or board[i][c] == n:
                return False
        
        # Check the 3x3 grid
        start_row, start_col = 3 * (r // 3), 3 * (c // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == n:
                    return False
        
        return True

    def solve(self, board):
        empty = self.find_empty(board)
        if not empty:
            return True  # No empty cell means the board is solved
        
        r, c = empty
        
        for n in map(str, range(1, 10)):  # Try numbers '1' to '9'
            if self.is_valid(board, r, c, n):
                board[r][c] = n
                
                if self.solve(board):  # Recursively solve the rest
                    return True
                
                board[r][c] = '.'  # Undo the move (backtrack)
        
        return False  # Trigger backtracking