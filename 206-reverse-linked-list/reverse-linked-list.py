# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ##we will  consider curr,nxt,prev
        curr=head
        nxt=None
        prev=None
        while(curr):
            nxt=curr.next
            curr.next=prev ##poinintg to null
            prev=curr ##pointing to first ele in iteration 1
            curr=nxt
        
        return prev
            
        