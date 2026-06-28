# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #Brute Force using recursion
        # result = []

        # def helper(node):
        #     if not node:
        #         return
        #     helper(node.left)
        #     helper(node.right)
        #     result.append(node.val)

        # helper(root)
        # return result



        #Using Stack 1- stack

        if not root:
            return []

        st = []

        curr = root
        res = []

        while (curr or st):
            if curr:
                st.append(curr)
                curr = curr.left
            else:
                tmp = st[-1].right
                if tmp:
                    curr = tmp
                else:
                    tmp = st.pop()
                    res.append(tmp.val)

                    while st and tmp == st[-1].right:
                        tmp = st.pop()  
                        res.append(tmp.val)
        return res