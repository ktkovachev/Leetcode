class Solution:
    def numSquares(self, n: int) -> int:
        # Possible square numbers we can choose from (all squares below n)
        squares_below = list(takewhile(lambda x: x <= n, (n ** 2 for n in count(1))))

        # Once this has been solved, it's basically just the same as 322. Coin Change
        minimum_to_make = [(n+1)] * (n + 1)  # List where the i'th index gives the number of squares required to make i
        minimum_to_make[0] = 0
        for i in range(n + 1):
            for num in squares_below:
                remainder = i - num
                if remainder >= 0:
                    minimum_to_make[i] = min(minimum_to_make[i], minimum_to_make[remainder] + 1)
        
        return minimum_to_make[-1]
