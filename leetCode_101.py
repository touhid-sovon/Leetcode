from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


left_sub = TreeNode(2, 3, 4)
root = TreeNode(1, None, left_sub)

root1 = TreeNode(1, None, 2)


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if root.left is None and root.right is None:
            return True
        if root.left is None or root.right is None:
            return False

        left_queue = [root.left]
        right_queue = [root.right]

        while left_queue and right_queue:
            left = left_queue.pop(0)
            right = right_queue.pop(0)

            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False

            left_queue.append(left.left)
            left_queue.append(left.right)
            right_queue.append(right.right)
            right_queue.append(right.left)

        return len(left_queue) == len(right_queue)


sol = Solution()
print(sol.isSymmetric(root1))



