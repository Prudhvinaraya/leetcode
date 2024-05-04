from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Step 1: Sort the array
        people.sort()
        
        # Step 2: Initialize pointers and count
        left, right = 0, len(people) - 1
        num_boats = 0
        
        # Step 3: Move pointers and count boats
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            num_boats += 1
        
        return num_boats