# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # 3 steps: find middle and split, reverse second half, merge

        if head == None:
            return

        # fast and slow pointers
        fast = head
        slow = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        curr = slow.next
        slow.next = None

        # reverse
        prev = None

        while curr != None:
            save = curr.next
            curr.next = prev
            prev = curr
            curr = save

        # merge
        first = head
        while prev != None and first != None:
            save1 = first.next
            save2 = prev.next
            first.next = prev
            prev.next = save1
            prev = save2
            first = save1

        




