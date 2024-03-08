class Solution:
    def check(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True

        decreasing_point = self.decreasing_point(nums)
        
        # Single sorted list
        if decreasing_point == len(nums):
            return True

        return self.decreasing_point(nums[decreasing_point:]) == len(nums) - decreasing_point and nums[-1] <= nums[0]

    def decreasing_point(self, nums: List[int]) -> int:
        decreasing_point = 1
        previous = nums[0]
        while decreasing_point < len(nums) and nums[decreasing_point] >= previous:
            previous = nums[decreasing_point]
            decreasing_point += 1
        
        return decreasing_point
