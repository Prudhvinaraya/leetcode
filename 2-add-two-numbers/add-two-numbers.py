class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy head to simplify edge cases
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        # Traverse both lists
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        # If there's still a carry, add a new node
        if carry:
            current.next = ListNode(carry)
        
        return dummy.next