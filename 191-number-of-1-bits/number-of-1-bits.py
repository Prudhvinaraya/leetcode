class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        bin_=bin(n)
        bin_=bin_[2:]
        for i in bin_:
            if i=='1':
                count+=1
        return count
        