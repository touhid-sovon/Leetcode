from typing import Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        queue = [(root, root.val)]
        while queue:
            node, level_sum = queue.pop(0)

            if node:
                if node.left:
                    queue.append((node.left, level_sum + node.left.val))
                if node.right:
                    queue.append((node.right, level_sum + node.right.val))

                if not node.left and not node.right:
                    if level_sum == targetSum:
                        return True

        return False


left_sub = TreeNode(2)
left_sub.left = TreeNode(4)
left_sub.right = TreeNode(5)
right_sub = TreeNode(3)
right_sub.left = TreeNode(6)
right_sub.right = TreeNode(7)
root = TreeNode(1, left_sub, right_sub)

sol = Solution()
print(sol.pathSum(root,8))