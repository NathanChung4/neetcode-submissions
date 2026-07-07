# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root) != -1

    def dfs(self, root: Optional[TreeNode]) -> int:
        # base case
        if not root:
            return 0
        
        leftDepth = self.dfs(root.left)
        rightDepth = self.dfs(root.right)

        if leftDepth == -1 or rightDepth == -1 or abs(leftDepth - rightDepth) > 1:
            return -1

        return max(leftDepth, rightDepth) + 1
