class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[counter]=nums[i]
                counter+=1
        for i in range(counter,len(nums)):
            nums[i]=0
        return nums
                
        