class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        lf=set(arr)
        current=1
        count=0
        while(True):
            if current not in lf:
                count+=1
                if count==k:
                    return current
            current+=1
        