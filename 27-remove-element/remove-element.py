class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[index]=nums[i]
                index+=1
        return index
                
#         k=0
#         for i in range(len(nums)):
#             if nums[i]==val:
#                 nums[i]=None
#         for i in range(len(nums)):
#             if nums[i]==None:
#                 k+=1
#         l=0
#         m=len(nums)-1
        
#         while(l<m):
#             if(nums[l]==None and nums[m]!=None):
#                 nums[l],nums[m]=nums[m],nums[l]
#                 l=l+1
#                 m=m-1
#             m=m-1
#         return k
    
        