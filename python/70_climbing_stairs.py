class Solution:
    def climbStairs(self, n: int) -> int:
        # Top-down linear programming approach, since we always have the choice
        # to either jump 1 step or 2, so the number of choices is just based
        # on the Fibonacci sequence.
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return b
