class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Step 1: Calculate the length of the linked list
        curr_node = head
        count = 0
        while curr_node:
            count += 1
            curr_node = curr_node.next
        
        # Handle edge case: Remove head node
        if n == count:
            return head.next
        
        # Calculate the position of the node to remove
        index = count - n
        
        # Step 2: Traverse to the node just before the one to remove
        curr_node = head
        for _ in range(index - 1):
            curr_node = curr_node.next
        
        # Step 3: Remove the nth node from the end
        curr_node.next = curr_node.next.next
        
        return head