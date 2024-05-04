class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # Initialize an array to store the number of distinct ways to reach each step
        dp = [0] * (n + 1)
        
        # Base cases
        dp[1] = 1
        dp[2] = 2
        
        # Iterate through the steps and calculate the number of distinct ways
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]

        