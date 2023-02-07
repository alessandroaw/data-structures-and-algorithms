class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        res = 1
        prev = 0

        while floor(res) != floor(prev):
            prev = res
            res = res - ((res * res - x)/(2 * res))

        return floor(res)
