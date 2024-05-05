class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # Copy the value of the next node to the current node
        node.val = node.next.val
        # Point the current node's next pointer to the next node's next pointer
        node.next = node.next.next