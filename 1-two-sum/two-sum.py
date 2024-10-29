class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #lets take 2 for loops and try to solve
        #nums is the given list
        #target is the target variable
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return i,j
        return -1
        