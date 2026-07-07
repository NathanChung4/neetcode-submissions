# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                if (i+1) > len(lists) -1:
                    merged.append(lists[i])           
                else:
                    merged.append(self.merge2Lists(lists[i], lists[i+1]))
            lists = merged
        
        return lists[0]
    
    def merge2Lists(self, list1: [ListNode], list2: [ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode()
        curr = dummyHead
        l1, l2 = list1, list2
        while l1 and l2:
            if l1.val > l2.val:
                curr.next = l2
                curr = curr.next
                l2 = l2.next
            else:
                curr.next = l1
                curr = curr.next
                l1 = l1.next
        if l1:
            curr.next = l1
        elif l2:
            curr.next = l2
        return dummyHead.next

