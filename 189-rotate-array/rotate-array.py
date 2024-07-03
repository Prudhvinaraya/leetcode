class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        """
        #incase k>len(array)
        n=len(nums)
        k=k%n
        
        nums[:]=nums[-k:]+nums[:-k]
        return nums
#         lst=[]
#         n=len(nums)
#         for i in range(k+1,n):
#             lst.append(nums[i])
#         for i in range(0,k+1):
#             lst.append(nums[i])
        
#         return lst
            