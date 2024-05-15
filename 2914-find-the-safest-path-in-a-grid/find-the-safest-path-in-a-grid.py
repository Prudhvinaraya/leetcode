from collections import deque

class Solution:
    def maximumSafenessFactor(self, grid):
        # Calculate safeness factors for each cell
        safeness = self.calculateSafenessFactors(grid)
        # Find the maximum safeness value from the safeness matrix
        maxSafeness = self.findMaxSafeness(safeness)
        # Perform binary search to find the maximum safeness factor
        return self.findMaxSafenessFactor(grid, safeness, maxSafeness)

    # Method to calculate the safeness factor for each cell using multi-source BFS
    def calculateSafenessFactors(self, grid):
        n = len(grid)
        safeness = [[float('inf')] * n for _ in range(n)]  # Initialize safeness matrix with infinity
        queue = deque()

        # Add all cells with gold to the queue and set their safeness to 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))
                    safeness[i][j] = 0

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Possible directions for movement

        # Perform BFS to calculate safeness factors
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                newX, newY = x + dx, y + dy
                # Check if the new cell is within bounds and update safeness if necessary
                if 0 <= newX < n and 0 <= newY < n and safeness[newX][newY] > safeness[x][y] + 1:
                    safeness[newX][newY] = safeness[x][y] + 1
                    queue.append((newX, newY))

        return safeness

    # Method to find the maximum safeness value from the safeness matrix
    def findMaxSafeness(self, safeness):
        return max(max(row) for row in safeness)

    # Method to perform binary search to find the maximum safeness factor
    def findMaxSafenessFactor(self, grid, safeness, maxSafeness):
        left, right, result = 0, maxSafeness, 0

        # Binary search to find the maximum safeness factor
        while left <= right:
            mid = left + (right - left) // 2
            # Check if the current mid value can be achieved
            if self.canAchieveSafeness(grid, safeness, mid):
                result = mid  # Update result if the current mid is achievable
                left = mid + 1
            else:
                right = mid - 1

        return result

    # Method to check if a path with the given safeness factor exists using BFS
    def canAchieveSafeness(self, grid, safeness, threshold):
        n = len(grid)
        if safeness[0][0] < threshold:  # If the starting cell's safeness is less than the threshold
            return False

        queue = deque([(0, 0)])  # Start BFS from the top-left corner
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Possible directions for movement

        # Perform BFS to check if the bottom-right corner can be reached
        while queue:
            x, y = queue.popleft()
            if x == n - 1 and y == n - 1:  # If we reach the bottom-right corner
                return True

            for dx, dy in directions:
                newX, newY = x + dx, y + dy
                # Check if the new cell is within bounds and its safeness is above the threshold
                if 0 <= newX < n and 0 <= newY < n and not visited[newX][newY] and safeness[newX][newY] >= threshold:
                    queue.append((newX, newY))
                    visited[newX][newY] = True

        return False