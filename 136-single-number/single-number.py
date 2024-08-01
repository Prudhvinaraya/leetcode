class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ##brute force using the dict
        dict_={}
        for i in nums:
            if i in dict_:
                dict_[i]+=1
            else:
                dict_[i]=1
        for key,value in dict_.items():
            if dict_[key]==1:
                return key
        
        