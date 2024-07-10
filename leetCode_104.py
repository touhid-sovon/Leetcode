from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


left_sub = TreeNode(2)
left_sub.left = TreeNode(3)
left_sub.right = TreeNode(4)
root = TreeNode(1, left_sub, left_sub)

root1 = TreeNode(1, None, 2)

# class Solution:
#     def maxDepth(self, root) -> int:
#         if not root:
#             return 0
#         depth = 1
#         max_depth = 0
#         node = root
#         stack = []
#         i = 1
#         while node:
#             print(f'{i}th iteration and node val {node.val}')
#             if node.left:
#                 print('c1')
#                 stack.append(node)
#                 node = node.left
#                 depth += 1
#             elif node.right:
#                 print('c2')
#                 stack.append(node)
#                 node = node.right
#                 depth += 1
#             else:
#                 tmp = node
#                 node = stack.pop()
#                 tmp = None
#                 print('after stack', node.val)
#                 depth -= 1
#             max_depth = max(max_depth,depth)
#             i += 1
#
#             if i == 6:
#                 break
#
#         return max_depth

class Solution:
    def maxDepth(self, root) -> int:
        if not root:
            return 0
        stack = [(root,1)]
        max_depth = 0

        while stack:
            node,depth = stack.pop()

            if node:
                max_depth = max(max_depth,depth)
                if node.right:
                    stack.append((node.right,depth+1))
                if node.left:
                    stack.append((node.left,depth+1))

        return max_depth

    # recursive solution
    '''
    def maxDepth(self,root)-> int:
        if not root:
            return 0
        return max(maxDepth(self.root.left),maxDepth(self.root.right)) + 1
    '''
sol = Solution()
print(sol.maxDepth(left_sub))

# node = root
#
# node.left = None
#
# if root.left:
#     print('some')
#
# print(root.left)