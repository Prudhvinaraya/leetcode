class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #i have nums array
        #i have target
        dict={}
        for i,j in enumerate(nums):
            dict[j] = i
        #[2:0,7:1.11:2,15:3]
        for i in range(len(nums)):
            if target-nums[i] in dict.keys() and dict[target-nums[i]]!=i:
                return i,dict[target-nums[i]]
            
        