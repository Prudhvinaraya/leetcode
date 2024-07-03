class Solution:
    def check(self, nums: List[int]) -> bool:
        #we are given an array of sorted and rotated by some count k 
        #first compare the adjacent elements and arr[i]>arr[i+1]
        #check that condition to be True so that anomoloies wont come if anomoloiges are >1 means we can give up for 1 time
        anomolie=0
        for i in range(len(nums)):
            if(nums[i]>nums[(i+1)%len(nums)]):
                anomolie+=1
            
        if anomolie >1:
            return False
        else :
            return True
