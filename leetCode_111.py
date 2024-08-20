from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = []
        depth = 2
        if not root.left and not root.right:
            return 1
        if root.left and not root.right:
            queue.append((root.left, depth))
        elif root.right and not root.left:
            queue.append((root.right, depth))
        else:
            queue.append((root.left, depth))
            queue.append((root.right, depth))

        max_depth = 2
        min_depth = 99999

        while queue:
            # print(depth)
            node, depth = queue.pop()

            if node:
                # max_depth = max(max_depth,depth)
                if node.right:
                    queue.append((node.right,depth+1))
                if node.left:
                    queue.append((node.left,depth+1))

                if not node.left and not node.right:
                    # print('leaf Node: ',node.val)
                    min_depth = min(min_depth,depth)

        return min_depth





left_sub = TreeNode(2,None,None)
#left_sub.left = TreeNode(5,None,None)
right_sub = TreeNode(3)
right_sub.left = TreeNode(4,None,None)
right_sub.left.left = TreeNode(8,None,None)
right_sub.right = TreeNode(7,None,None)
root = TreeNode(1, left_sub, right_sub)

sol = Solution()
print(sol.minDepth(root))