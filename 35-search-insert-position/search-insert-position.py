class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i]==target:
                return i
            else:
                nums.append(target)
                nums = sorted(nums)
                for i in range(len(nums)):
                    if nums[i]==target:
                        return i

