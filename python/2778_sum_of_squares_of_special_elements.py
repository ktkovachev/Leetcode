class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        return sum(x**2 for (i, x) in enumerate(nums) if n % (i+1) == 0)
