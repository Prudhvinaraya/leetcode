# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ##find the middle element using tortoise and hare method
        fast=head
        slow=head
        curr_node=head
        while(fast and fast.next):
            curr_node=slow
            slow=slow.next
            fast=fast.next.next
        if curr_node == fast== slow:
            return None
        curr_node.next=slow.next
        slow.next=None
        return head
        