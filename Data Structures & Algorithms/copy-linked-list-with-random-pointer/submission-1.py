"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        # two pass technique
        # pass 1: iterate through list, copy nodes, and construct hashmap
        # pass 2: assign the nodes next and random pointers to match old list

        # pass 1
        linkMap = {}
        old_node = head
        while old_node:
            new_node = Node(old_node.val)
            linkMap[old_node] = new_node
            old_node = old_node.next

        # pass 2
        old_node = head
        while old_node:
            new_node = linkMap.get(old_node)
            new_node.next = linkMap.get(old_node.next)
            new_node.random = linkMap.get(old_node.random)
            old_node = old_node.next

        return linkMap.get(head)



