from typing import List

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        max_abs = -1  # Initialize maximum absolute value
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == 0:
                    max_abs = max(max_abs, abs(nums[i]))  # Update maximum absolute value
        return max_abs
