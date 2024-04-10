from collections import deque
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
            # Sort the deck in ascending order
        deck.sort()
        n = len(deck)
        
        # Initialize a queue with indices from 0 to n-1
        index_queue = deque(range(n))
        
        # Initialize the result list
        result = [0] * n
        
        # Simulate the process of revealing cards
        for card in deck:
            # Take the index from the front of the queue
            front_index = index_queue.popleft()
            # Assign the current card to the result list at the taken index
            result[front_index] = card
            # If there are still unrevealed cards, move the next index to the back of the queue
            if index_queue:
                next_index = index_queue.popleft()
                index_queue.append(next_index)
        
        return result
