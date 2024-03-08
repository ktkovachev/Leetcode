# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if nums == []:
            return None

        mid = len(nums)//2
        left = nums[:mid]
        right = nums[mid+1:]

        head = TreeNode(nums[mid])
        head.left = self.sortedArrayToBST(left)
        head.right = self.sortedArrayToBST(right)
        return head
