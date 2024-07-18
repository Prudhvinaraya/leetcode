# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Opitmal approach
        if not head or not head.next :
            return head
        odd=head
        evenhead=head.next
        even=head.next
        while(even and even.next):
            odd.next=odd.next.next
            even.next=even.next.next
            odd=odd.next
            even=even.next
        if odd:
            odd.next
            
        odd.next=evenhead
        return head
        
        # ##BRUTE FORCE
        # if not head or not head.next:  #->Base case
        #     return head
        # lst=[]
        # odd=head
        # even=head.next
        # while(odd and odd.next):
        #     lst.append(odd.val)
        #     odd=odd.next.next
        # if(odd):
        #     lst.append(odd.val)
        # while(even and even.next):
        #     lst.append(even.val)
        #     even=even.next.next
        # if (even):
        #     lst.append(even.val)
        # curr=head
        # i=0
        # while(curr):
        #     curr.val=lst[i]
        #     i+=1
        #     curr=curr.next
        # return head
            
            
            
                
        
        