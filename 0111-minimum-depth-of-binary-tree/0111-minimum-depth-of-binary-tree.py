# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        if not root.left:
            return self.minDepth(root.right) + 1
        
        if not root.right:
            return self.minDepth(root.left) + 1
        
        leftDepth = self.minDepth(root.left)
        rightDepth = self.minDepth(root.right)
        
        return min(leftDepth, rightDepth) + 1