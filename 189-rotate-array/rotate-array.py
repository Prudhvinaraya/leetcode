class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # Handle cases where k >= n

        if k == 0:
            return
        
        # Correct slicing: Last k elements move to the front
        nums[:] = nums[-k:] + nums[:-k]
        