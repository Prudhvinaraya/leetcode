# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ##Bruteforce
        curr_node=head
        count=0
        while(curr_node):
            count+=1
            curr_node=curr_node.next
        ##count=5
        if count==1:
            return None
        if count==n:
            return head.next
        index=count-n ##3
        curr_node=head
        c=0
        for _ in range(index - 1):
            curr_node = curr_node.next
        curr_node.next=curr_node.next.next
        return head
        