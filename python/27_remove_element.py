class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        for i in range(n-1, -1, -1):
            if nums[i] == val:
                del nums[i]
                n -= 1
        return n
