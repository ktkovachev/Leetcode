class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        negative_end = 0
        while negative_end < len(nums) and nums[negative_end] < 0:
            negative_end += 1

        return self.merge(
            [x ** 2 for x in reversed(nums[:negative_end])],
            [x ** 2 for x in nums[negative_end:]]
        )
    
    def merge(self, list1: List[int], list2: List[int]) -> List[int]:
        left1 = 0
        left2 = 0
        new = []

        while left1 < len(list1) and left2 < len(list2):
            if list1[left1] < list2[left2]:
                new.append(list1[left1])
                left1 += 1
            else:
                new.append(list2[left2])
                left2 += 1

        while left1 < len(list1):
            new.append(list1[left1])

        while left2 < len(list2):
            new.append(list1[left1])

        return new


"""
Alternative solution with the work done manually to save on unneeded copying

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = len(nums)

        negative_end = 0
        while negative_end < l and nums[negative_end] < 0:
            negative_end += 1
        
        # Square the array
        for i in range(l):
            nums[i] = nums[i] ** 2

        # Reverse the negative part of the array
        for i in range(negative_end // 2):
            nums[i], nums[negative_end-i-1] = nums[negative_end-i-1], nums[i]
        

        # Merge the parts together
        new = []

        left = 0
        right = negative_end

        while left < negative_end and right < l:
            if nums[left] < nums[right]:
                new.append(nums[left])
                left += 1
            else:
                new.append(nums[right])
                right += 1

        while left < negative_end:
            new.append(nums[left])
            left += 1

        while right < l:
            new.append(nums[right])
            right += 1

        return new

"""