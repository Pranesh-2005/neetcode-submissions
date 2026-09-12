# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indx = {v:i for i,v in enumerate(inorder)}
        preIdx = 0
        def build(l,r):
            nonlocal preIdx
            if l >= r:
                return None
            root = TreeNode(preorder[preIdx])
            preIdx += 1
            m = indx[root.val]
            root.left = build(l,m)
            root.right = build(m+1,r)
            return root
        return build(0, len(inorder))
        


        