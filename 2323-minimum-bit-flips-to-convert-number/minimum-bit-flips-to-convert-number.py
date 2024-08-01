class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        #find the xor of start ,goal
        #find the no of set bits
        #->1
        ans=start^goal
        ans=bin(ans)
        ans=ans[2:]
        count=0
        for i in ans:
            if i=='1':
                count+=1
        return count
            
        
        