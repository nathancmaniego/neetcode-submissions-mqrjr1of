"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        oldToNew = {}
        oldToNew[node] = Node(node.val)
        q = [node]
        while q:
            cur = q.pop(0)
            for n in cur.neighbors:
                if n not in oldToNew:
                    oldToNew[n] = Node(n.val)
                    q.append(n)
                oldToNew[cur].neighbors.append(oldToNew[n])
        return oldToNew[node]