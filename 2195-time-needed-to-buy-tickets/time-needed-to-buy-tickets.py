class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0
        while(tickets[k] != 0):
            i=0
            while(i<len(tickets)):
                tickets[i] -= 1
                count += 1
                #print(count,tickets,k)
                if tickets[k] == 0:
                    break
                if tickets[i] == 0:
                    if i < k:
                        k -= 1
                    del tickets[i]
                else:
                    i+=1       
        return count