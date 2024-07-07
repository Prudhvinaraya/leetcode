class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        res_1_count = 0
        res_0_count = 0
        curr_1_count = 0
        curr_0_count = 0
        
        for char in s:
            if char == "1":
                curr_1_count += 1
                curr_0_count = 0  # Reset zero count
                res_1_count = max(res_1_count, curr_1_count)
            elif char == "0":
                curr_0_count += 1
                curr_1_count = 0  # Reset one count
                res_0_count = max(res_0_count, curr_0_count)
        
        return res_1_count > res_0_count
