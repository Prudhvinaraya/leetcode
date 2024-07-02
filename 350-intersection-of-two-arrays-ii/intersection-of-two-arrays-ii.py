class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #sort the lists
        nums1=sorted(nums1)
        nums2=sorted(nums2)
        #compare the two lists and append into a list
        i,j=0,0
        lst=[]
        while i<len(nums1) and j<len(nums2):
            #if both the values at same indexs are same 
            if nums1[i]==nums2[j]:
                lst.append(nums1[i])
                i+=1
                j+=1
            #the values at same index are not same and if nums1 have more value then we have to update the counter of nums2 so that in next itertion we can compare nums1[current] with next of nums2
            elif nums1[i]>nums2[j]:
                j+=1
            else:
                i+=1
        return lst