# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # create the queue, outer loop, save length

        if not root:
            return []
        queue = collections.deque([root])

        res = []

        while queue:
            temp = []
            for i in range(len(queue)):
                front = queue.popleft()
                temp.append(front.val)
                if front.left:
                    queue.append(front.left)
                if front.right:
                    queue.append(front.right)

            res.append(temp)

        return res    