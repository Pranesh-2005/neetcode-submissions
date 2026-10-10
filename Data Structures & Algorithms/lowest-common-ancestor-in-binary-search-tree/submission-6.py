# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(root):
            if not root or p is root or q is root:
                return root
            left = dfs(root.left)
            right = dfs(root.right)
            if left and right:
                return root
            return left or right
        return dfs(root)