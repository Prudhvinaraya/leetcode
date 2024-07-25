class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lst=nums1+nums2
        lst.sort()
        l=len(lst)
        m=l//2
        if l%2==0:
            return (lst[m-1]+lst[m])/2.0
        else:
            return float(lst[m])
        