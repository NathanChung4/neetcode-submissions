# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # if empty
        if not root:
            return ""

        queue = collections.deque()
        queue.append(root)
        res = []

        while queue:
            node = queue.popleft()
            if not node:
                res.append("N")
            else:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
                
        res = ",".join(res)
        return res
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        #if empty
        if data == "":
            return None
        
        queue = collections.deque()
        
        dataList = data.split(",")

        if dataList[0] == "N":
            return None
        else:
            root = TreeNode(int(dataList[0]))
        
        queue.append(root)
        i = 1
        while queue:
            node = queue.popleft()
            if dataList[i] == "N":
                node.left = None
            else:
                node.left = TreeNode(int(dataList[i]))
                queue.append(node.left)

            if dataList[i+1] == "N":
                node.right = None
            else:
                node.right = TreeNode(int(dataList[i+1]))
                queue.append(node.right)
            
            i+=2

        return root
