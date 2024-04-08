class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lower = 0
        upper = len(nums)-1
        while True:
            mid = (upper + lower) // 2
            if nums[mid] == target:
                return mid
            elif mid == 0 and nums[mid] > target:
                return mid
            elif mid >= len(nums) - 1:
                if nums[mid] < target:
                    return mid + 1
                else:
                    return mid
            elif nums[mid] > target and nums[mid-1] < target:
                return mid
            elif nums[mid] < target:
                lower = mid + 1
            else:
                upper = mid - 1
