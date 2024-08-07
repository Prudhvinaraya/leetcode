class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n=len(s1)
        dp=[[[False for _ in range(n)] for _ in range(n)] for _ in range(n+1)]
        for i in range(n):
            for j in range(n):
                dp[1][i][j]=s1[i]==s2[j]
        for length in range(2,n+1):
            for i in range(n+1-length):
                for j in range(n+1-length):
                    for newlength in range(1,length):
                        dp1=dp[newlength][i]
                        dp2=dp[length-newlength][i+newlength]
                        dp[length][i][j] |=dp1[j] and dp2[j+newlength]
                        dp[length][i][j] |=dp1[j+length-newlength] and dp2[j]
        return dp[n][0][0]
            
        
        