# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorderInner(root: Optional[TreeNode], out: List[int]):
            if root is None: return out
            inorderInner(root.left, out)
            out.append(root.val)
            return inorderInner(root.right, out)
        return inorderInner(root, [])
