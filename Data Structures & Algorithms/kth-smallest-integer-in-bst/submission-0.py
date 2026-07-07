# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self, count = 0, result = 0):
        self.count = count
        self.result = result

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        return self.dfs(root, k)
    
    def dfs(self, node: Optional[TreeNode], kVal: int):
        # base case
        if not node:
            return

        if self.count == kVal:
            return self.result

        # step 1: recurse left
        self.dfs(node.left, kVal)

        # step 2: do work at node
        self.count += 1

        if self.count == kVal:
            self.result = node.val
            return self.result

        # step 3: recurse right
        self.dfs(node.right, kVal)

        return self.result

