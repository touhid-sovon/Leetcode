from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# node 1
tree1 = TreeNode(1)
left1 = TreeNode(2)
right1 = TreeNode(3)

tree1.left = left1
tree1.right = right1

# node 2
tree2 = TreeNode(1)
left2 = TreeNode(2)
right2 = TreeNode(3)

tree2.left = left2
tree2.right = right2

list1 = []
list2 = []

list1.append(tree1)
list2.append(tree2)
print(list1)
print(list2)

print(list1.pop(0).val)


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = []
        q2 = []
        q1.append(p)
        q2.append(q)

        while q1 and q2:
            tree1 = q1.pop(0)
            tree2 = q2.pop(0)

            if tree1 is None and tree2 is None:
                continue
            elif tree1 is None or tree2 is None:
                return False

            if tree1.val != tree2.val:
                return False

            q1.append(tree1.left)
            q1.append(tree1.right)
            q2.append(tree2.left)
            q2.append(tree2.right)

        return True

sol = Solution()

print(sol.isSameTree(tree1, tree2))
