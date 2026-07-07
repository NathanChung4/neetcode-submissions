# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # 4 operations
        # save next pointer
        # flip pointer
        # advance prev
        # advance curr

        curr = head
        prev = None

        while curr != None:
            
            
            nextP = curr.next
            curr.next = prev
            prev = curr
            curr = nextP

        return prev
                
