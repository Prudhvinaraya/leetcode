class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        set_=set(nums)
        #set_=set(map(int,set_))
        for i in range(len(nums)+1): #i->
            if i not in set_:
                return i
        return -1
                
        