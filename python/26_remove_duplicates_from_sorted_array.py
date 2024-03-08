class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current = nums[-1] + 1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == current:
                del nums[i]
            else:
                current = nums[i]
        return len(nums)