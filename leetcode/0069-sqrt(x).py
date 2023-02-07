class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        res = 1
        prev = res
        n = 0
        for i in range(100):
            n = i
            res = res - ((res * res - x)/(2 * res))
            if floor(prev) == floor(res):
                break
            prev = res
        return floor(res)
