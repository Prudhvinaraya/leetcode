# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ##Brute force 0(n+n/2)
        # curr_node=head
        # count=0
        # # lst=[]
        # while(curr_node != None):
        #     curr_node=curr_node.next
        #     count+=1
        # ##i got count =5
        # curr_node=head
        # c=0
        # while(curr_node!=None and c!=count//2):
        #     c+=1
        #     curr_node=curr_node.next
        # head=curr_node
        
        
        ##optimal solution using tortoise and hare method
        slow=head
        fast=head
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
        return slow
        
        