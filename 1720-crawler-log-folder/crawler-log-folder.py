class Solution:
    def minOperations(self, logs: List[str]) -> int:
        step=0
        
        for i in range(len(logs)):
            if logs[i]=="../":
                step-=1
                step=max(0,step)
            elif logs[i]=="./":
                step=step
            else:
                step+=1
        return step
                
        