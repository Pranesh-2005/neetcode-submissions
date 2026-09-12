# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(root,min,max):
            if not root:
                return True
            if not (root.val > min and root.val < max):
                return False
            return check(root.left,min,root.val) and check(root.right,root.val,max)
        return check(root,float("-inf"),float("inf"))
        