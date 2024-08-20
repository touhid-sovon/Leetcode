from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #     if not root:
    #         return root
    #     if not root.left and root.right:
    #         return root
    #     queue = [root]
    #     for i, node in enumerate(queue):
    #         if node.left:
    #             queue.append(node.left)
    #         if node.right:
    #             queue.append(node.right)
    #     # node_list = [node.val for node in queue]
    #     # print(node_list)
    #
    #     i, j = 1, 0
    #     n = len(queue)
    #     while j < n:
    #         node = queue[j]
    #         #print(node.val)
    #         if node.right:
    #             node.right = queue[i]
    #             i += 1
    #         if node.left:
    #             node.left = queue[i]
    #             i += 1
    #         j += 1
    #     return root
    class Solution:
        def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
            if root is None:
                return root

            # Use a queue for BFS traversal
            queue = [root]

            while queue:
                current = queue.pop(0)

                # Swap the left and right children
                current.left, current.right = current.right, current.left

                # Add the children to the queue if they exist
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

            return root

    def show(self, root):
        if not root:
            return root
        queue = [root]
        for i, node in enumerate(queue):
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        level = [node.val for node in queue]
        print(level)




left_sub = TreeNode(2)
left_sub.left = TreeNode(1,None,None)
left_sub.right = TreeNode(3,None,None)
right_sub = TreeNode(7)
right_sub.left = TreeNode(6,None,None)
# right_sub.left.left = TreeNode(8,None,None)
right_sub.right = TreeNode(9,None,None)
root = TreeNode(4, left_sub, right_sub)

test = TreeNode(1)
test.left = TreeNode(2,None,None)
test.right = TreeNode(None)
sol = Solution()
sol.invertTree(test)
sol.show(test)
