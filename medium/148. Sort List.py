# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



head = ListNode(4,ListNode(2,ListNode(1,ListNode(3))))

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        val = head
        while val.next:
            lst.append(val.val)
            val=val.next
        lst = list(sorted(lst))
        new_head = ListNode(lst[0])
        for i in range(lst-1):  
            
        return head
sol = Solution()
sol.sortList(head)