# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lvlorder(self, root):
        if not root:
            return []
        res, q = [], deque([root])
        while q:
            lvl = []
            for _ in range(len(q)):
                node = q.popleft()
                lvl.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(lvl)
        return res
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        return [lvl[-1] for lvl in self.lvlorder(root)]
        