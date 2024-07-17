# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        ##brute force
#         dict={}
#         curr_node=head
#         while(curr_node):
#             if curr_node in dict:
#                 return curr_node
#             dict[curr_node]=True
#             curr_node=curr_node.next
        ##optimal
        #1)Detect the loop using tortoise and hare method
        slow=head
        fast=head
        while(fast is not None and fast.next is not None):
            slow=slow.next
            fast=fast.next.next
            if (slow==fast):
                ##yes there is loop
                #2)Task is to find the start of the loop
                slow=head
                while(slow!=fast):
                    slow=slow.next
                    fast=fast.next
                return slow
        return None
        