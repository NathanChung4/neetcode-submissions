# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # fast and slow pointers
        slow, fast = head, head

        # give fast pointer head start
        count = 0
        while count < n:
            fast = fast.next
            count += 1
        if fast == None:
            head = head.next
            return head
        
        # advance both pointers
        while fast.next:
            slow = slow.next
            fast = fast.next

        # rewire pointers
        slow.next = slow.next.next

        return head



