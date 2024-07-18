class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        curr = head
        
        # Collect values from the linked list
        while curr:
            lst.append(curr.val)
            curr = curr.next
        
        # Sort the values
        lst.sort()
        
        # Update the linked list with sorted values
        curr = head
        i = 0
        while curr:
            curr.val = lst[i]
            i += 1
            curr = curr.next
        
        return head