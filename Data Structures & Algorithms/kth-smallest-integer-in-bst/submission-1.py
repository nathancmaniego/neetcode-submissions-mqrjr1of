# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root):
            lst = []
            if root is None:
                return []
            if root.left is None and root.right is None:
                lst.append(root.val)
                return lst
            if root.left:
                lst.extend(dfs(root.left))
            lst.append(root.val)
            if root.right:
                lst.extend(dfs(root.right))
            return lst
        return dfs(root)[k-1]