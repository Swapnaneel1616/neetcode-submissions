# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxCheck(self , node , diameter):
        if not node:
            return 0
        left = self.maxCheck(node.left , diameter)
        right = self.maxCheck(node.right, diameter)

        diameter[0] = max(diameter[0], left+right)
        return max(left , right) + 1
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0]
        self.maxCheck(root , diameter)
        return diameter[0]