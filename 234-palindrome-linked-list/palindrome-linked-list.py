# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True
        ##first find the mid
        slow=head
        fast=head
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
        curr=slow
        prev=None
        
        ##write the logic for reverse
        nxt=None
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        first_half=head
        second_half=prev
        while(second_half):
            if(first_half.val!=second_half.val):
                return False
            first_half=first_half.next
            second_half=second_half.next
        return True
                
        
        