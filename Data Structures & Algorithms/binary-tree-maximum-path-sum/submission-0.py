# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.sum = float('-inf')

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.sum

    def dfs(self, node) -> int:
        # base case
        if not node:
            return 0
        
        # calculate left
        leftVal = max(self.dfs(node.left), 0)
        # right
        rightVal = max(self.dfs(node.right),0)

        self.sum = max(self.sum, leftVal + rightVal + node.val)
        return node.val + max(leftVal, rightVal)


        