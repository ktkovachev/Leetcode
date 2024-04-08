class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        end = len(s)-1
        while end >= 0 and s[end] == " ":
            end -= 1
        i = end
        while i >= 0 and s[i] != " ":
            i -= 1
        return end-i
