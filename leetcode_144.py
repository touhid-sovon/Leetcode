from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ''' One way '''
    # def preorderTraversal(self, root: Optional[TreeNode],res=None) -> list[int]:
    #     if not res:
    #         res = []
    #     if not root:
    #         return res
    #
    #     res.append(root.val)
    #     self.preorderTraversal(root.left,res)
    #     self.preorderTraversal(root.right,res)
    #
    #     return res

    ''' Second Method '''
    # def preorderTraversal(self,root:Optional[TreeNode]) -> list[int]:
    #     res = []
    #
    #     if not root:
    #         return res
    #
    #     res.append(root)
    #     res += self.preorderTraversal(root.left)
    #     res += self.preorderTraversal(root.right)
    #
    #     return res

    ''' Optimized way '''
    def preorderTraversal(self,root:Optional[TreeNode]) -> list[int]:
        res  = []
        if not root:
            return res

        stack = [root]

        while stack:
            curr_node = stack.pop()
            res.append(curr_node.val)

            # last in first order
            if curr_node.right:
                stack.append(curr_node.right)

            if curr_node.left:
                stack.append(curr_node.left)

        return res
