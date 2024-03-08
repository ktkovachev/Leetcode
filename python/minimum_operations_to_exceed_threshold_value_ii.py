class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        operations = 0
        while (x := heappop(nums)) < k:
            y = heappop(nums)
            heappush(nums, min(x,y)*2 + max(x,y))
            operations += 1
        return operations