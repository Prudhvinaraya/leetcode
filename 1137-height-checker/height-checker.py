class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        count=0
        x=sorted(heights)
        for i in range(len(x)):
            if(x[i]!=heights[i]):
                count+=1
        return count