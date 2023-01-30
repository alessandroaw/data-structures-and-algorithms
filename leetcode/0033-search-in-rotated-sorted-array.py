class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        t = target
        while l <= r:
            m = (l + r) // 2
            cm = nums[m]
            cl = nums[l]
            cr = nums[r]

            if cm == t:
                return m

            if cl <= cm:
                if t < cl or t > cm:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if t > cr or t < cm:
                    r = m - 1
                else:
                    l = m + 1

        return -1
