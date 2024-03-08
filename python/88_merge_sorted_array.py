class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        current = m + n - 1  # Pointer where we are currently inserting elements
        left = m - 1         # Pointer to the largest remaining element in nums1
        right = n - 1        # Pointer to the largest remaining element in nums2

        while left >= 0 and right >= 0:
            if nums1[left] > nums2[right]:
                nums1[current] = nums1[left]
                left -= 1
            else:
                nums1[current] = nums2[right]
                right -= 1
            current -= 1

        while left >= 0:
            nums1[current] = nums1[left]
            left -= 1
            current -= 1

        while right >= 0:
            nums1[current] = nums2[right]
            right -= 1
            current -= 1
