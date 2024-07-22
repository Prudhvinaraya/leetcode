# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        currA=headA
        currB=headB
        c1=0
        c2=0
        ##edge case
        if (currA==None or currB==None):
            return None
        
        ##calculate the length of each ll
        while(currA):
            currA=currA.next
            c1+=1 #->5
        while(currB):
            currB=currB.next
            c2+=1 #->6
        ##so we got the two ll lengths
        currA=headA
        currB=headB
        if (c1<c2):
            d=c2-c1
            while(d):
                currB=currB.next
                d-=1
            while(currB and currA):
                if currA==currB:
                    return currA
                currA=currA.next
                currB=currB.next
            return None
        else:
            d=c1-c2
            while(d):
                currA=currA.next
                d-=1
            while(currA and currB):
                if currA==currB:
                    return currA
                currA=currA.next
                currB=currB.next
            return None
            
            
                
        
        