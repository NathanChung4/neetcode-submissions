# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        self.dfs(root, float('-inf'))
        return self.count
    
    def dfs(self, current: TreeNode, maxSeen: int) -> int:
        if not current:
            return 0
        
        if current.val >= maxSeen:
            self.count += 1
        
        return self.dfs(current.left, max(maxSeen, current.val)) + self.dfs(current.right, max(maxSeen, current.val))