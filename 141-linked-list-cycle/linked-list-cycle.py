# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ##cycle is there or not
        slow=head
        fast=head
        while(fast!=None and fast.next!=None): ##->we are checking that our linkedlist has At least two nodes for moving fast pointer 
            slow=slow.next
            fast=fast.next.next
            if slow ==fast:
                return True
        return False
            
            
            
        
        