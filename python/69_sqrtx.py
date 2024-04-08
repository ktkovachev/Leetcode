class Solution:
    def mySqrt(self, x: int) -> int:
        # Use Newton-Raphson iteration
        # y**2 - x = 0 = f(y)
        # f'(y) = 2y
        # y = y - (y**2 - x)/(2y)
        y = 1
        close_enough = False
        while not close_enough:
            y -= (y*y-x)/(2*y)
            close_enough = y*y - x <= 0.1 and (y+1)*(y+1) > x
        return floor(y)
