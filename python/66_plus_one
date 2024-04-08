class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for current_index in range(len(digits)-1, -1, -1):
            carry, digits[current_index] = divmod(digits[current_index]+carry, 10)
            current_index -= 1
        if carry == 1:
            digits.insert(0, 1)
        return digits
