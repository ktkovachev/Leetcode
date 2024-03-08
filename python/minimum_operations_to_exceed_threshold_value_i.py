class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        operations = 0
        while heappop(nums) < k:
            operations += 1
        return operations
