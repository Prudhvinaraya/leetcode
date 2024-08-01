class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        #find the xor of start ,goal
        #find the no of set bits
        #-2
        xor_=start^goal
        count=0
        while xor_:
            count+=xor_ &1
            xor_=xor_>>1
        return count
    
        
        #->1
        # ans1=start^goal
        # ans=bin(ans1)
        # ans=ans[2:]
        # count=0
        ##counting the number of flip bits
        # for i in ans:
        #     if i=='1':
        #         count+=1
        
        #return count
            
        
        