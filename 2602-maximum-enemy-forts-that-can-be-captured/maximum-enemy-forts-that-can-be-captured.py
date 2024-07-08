class Solution:
    def captureForts(self, forts: List[int]) -> int:
        maxCaptures, currCaptures, myFort, unoccupied = 0, 0, False, False
        for fort in forts:
            if fort == 1:
                if unoccupied:
                    maxCaptures=max(currCaptures, maxCaptures) 
                myFort, unoccupied, currCaptures = True, False, 0
            elif fort == -1:
                if myFort:
                    maxCaptures = max(currCaptures, maxCaptures)
                myFort, unoccupied, currCaptures = False, True, 0
            elif (myFort or unoccupied) and fort == 0:
                currCaptures+=1  
        return maxCaptures 