# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # if root is None:
        #     return []
        
        # return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

        #Iterative approach 

        st = []

        node = root
        inorder = []

        while True:
            if node is not None:
                st.append(node)
                node = node.left
            
            else:
                if not st:
                    break
                node = st.pop()
                inorder.append(node.val)
                node = node.right
        return inorder