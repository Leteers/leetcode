from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 2
        val = head.next
        while val != None:
            val = val.next
            print(length)
            length += 1
            
        if length%2==0:
            mid = length//2+1
        else:
            mid = length//2
        
        result = head.next
        i = 1
        while i < mid:
            i += 1
            result = result.next
            print(result)
            
            
        return(result) 
        
        
head = [1,2,3,4,5]