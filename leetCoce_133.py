
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldTonew = {}  #hashmap

        def dfs(node):
            if node in oldTonew:
                return oldTonew[node]

            clone = Node(node.val)
            oldTonew[node] = clone

            for nei in node.neighbors:
                clone.neighbors.append(dfs(nei))
            return clone

        return dfs(node) if node else None

sol = Solution()

print(sol.cloneGraph([[2,4],[1,3],[2,4],[1,3]]))
