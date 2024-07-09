class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        ##Bruteforce approach
        #Traverse through the array
        p=0
        n=0
        for i in nums:
            if i==0:
                pass
            elif i>0:
                p+=1
            else:
                n+=1
        return max(p,n)
        