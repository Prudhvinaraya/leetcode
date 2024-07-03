class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        """
        #two pointer concept
        intial=0
        if(len(nums))<2:
            return nums

        #move the non-zerod to front 
        for j in range(len(nums)):
            if nums[j]!=0:
                nums[intial]=nums[j]
                intial+=1
        for f in range(intial,len(nums)):
            nums[f]=0
        
            
        return nums
        
        
        