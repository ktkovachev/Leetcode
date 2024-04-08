# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def hasPathSumInner(root: Optional[TreeNode], currentSum: int) -> bool:
            if root is None:
                return False
            elif root.left is None and root.right is None:
                return currentSum + root.val == targetSum
            else:
                newSum = currentSum + root.val
                return hasPathSumInner(root.left, newSum) or hasPathSumInner(root.right, newSum)
        return hasPathSumInner(root, 0)
