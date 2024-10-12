from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ''' Recursive way '''
    # def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
    #     res = []
    #     if not root:
    #         return []
    #
    #     res.extend(self.postorderTraversal(root.left))
    #     res.extend(self.postorderTraversal(root.right))
    #     res.append(root.val)
    #
    #     return res

    ''' Iterative way'''
    def postorderTraversal(self,root:Optional[TreeNode]) -> list[int]:
        res = []

        if not root:
            return res

        queue = [root]

        while queue:
            curr_node = queue.pop(0)
            if curr_node.right:
                res.
