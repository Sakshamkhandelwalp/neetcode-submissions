# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        t = head 
        m = head
        count = 0
        while t is not None:
            count +=1 
            t = t.next 
        k = count - n 
        if k == 0:
            return head.next
        for i in range(k - 1):
            m = m.next
        m.next = m.next.next
        return head