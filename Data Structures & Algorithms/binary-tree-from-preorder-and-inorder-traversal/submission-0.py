# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # create hashmap
        seen = {}
        for i, val in enumerate(inorder):
            seen[val] = i
        return self.dfs(0, len(preorder)-1, 0, len(inorder)-1, preorder, inorder, seen)


    def dfs(self, leftPre, rightPre, leftIn, rightIn, preorder, inorder, seen):
        # base case
        if leftPre > rightPre:
            return None
        
        root = TreeNode(preorder[leftPre])
        mid = seen.get(preorder[leftPre])
        k = mid - leftIn
        root.left = self.dfs(leftPre+1, leftPre+mid-leftIn, leftIn, mid-1, preorder, inorder, seen)
        root.right = self.dfs(leftPre+mid-leftIn+1, rightPre, mid+1, rightIn, preorder, inorder, seen)

        return root
