# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []

        queue = collections.deque([root])
        res = []

        while queue:
            length = len(queue)
            for i in range(length):
                front = queue.popleft()
                if front.left:
                    queue.append(front.left)
                if front.right:
                    queue.append(front.right)
                if i == length - 1:
                    res.append(front.val)
        
        return res
                
