# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(rootNode:object()):
    if not rootNode:
        return
    queueNode = []
    queueNode.append(rootNode)
    while queueNode:
        root = queueNode.pop(0)
        print(root.val)
        if root.left:
            queueNode.append(root.left)
        if root.right:
            queueNode.append(root.right)



leaf = TreeNode(3)
parent = TreeNode(2,leaf,None)
root = TreeNode(1,None,parent)

#level_order(root)




class Solution:
    def inorderTraversal(self, root) -> list[int]:
        res = []
        def traverseLeft(node):
            if not node:
                return
            traverseLeft(node.left)
            res.append(node.val)
            traverseLeft(node.right)
        traverseLeft(root)
        return res
sol = Solution()

print(sol.inorderTraversal(root))
