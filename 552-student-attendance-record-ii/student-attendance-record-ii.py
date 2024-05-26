class Solution:
    def checkRecord(self, n: int) -> int:   
        mod=10**9+7
        dp=[[[0 for _ in range (2) ] for _ in range(3)] for _ in range(n+1)]
        dp[1][0][0]=1
        dp[1][0][1]=1
        dp[1][1][0]=1
        dp[1][1][1]=0
        dp[1][2][0]=0
        dp[1][2][1]=0        
        for i in range (2,n+1):
            dp[i][0][0] = (dp[i-1][0][0] + dp[i-1][1][0] + dp[i-1][2][0]) % mod
            dp[i][0][1] = (dp[i-1][0][0] + dp[i-1][1][0] + dp[i-1][2][0]) % mod+ (dp[i-1][0][1] + dp[i-1][1][1] + dp[i-1][2][1]) %mod
            dp[i][1][0] = dp[i-1][0][0] % mod
            dp[i][1][1] = dp[i-1][0][1] % mod
            dp[i][2][0] = dp[i-1][1][0] % mod
            dp[i][2][1] = dp[i-1][1][1] % mod
            
        ans=0
        for i in range(3):
            for j in range(2):
                ans+=dp[-1][i][j]
                ans%=mod
                
        return ans 