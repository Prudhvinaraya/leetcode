class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        ##Bruteforce approach
        #Traverse through the array
        p=0  #0(1)
        n=0  #0(1)
        for i in nums:  #(n)
            if i==0:
                pass
            elif i>0:
                p+=1
            else:
                n+=1
        return max(p,n) #0(n)
        