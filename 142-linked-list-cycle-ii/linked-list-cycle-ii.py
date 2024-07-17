# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dict={}
        curr_node=head
        while(curr_node):
            if curr_node in dict:
                return curr_node
            dict[curr_node]=True
            curr_node=curr_node.next
        