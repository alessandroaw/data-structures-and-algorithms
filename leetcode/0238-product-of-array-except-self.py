# array and hashing
# TC: O(n)
# SC: O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        # output 23 13 12
        # input 1 2 3
        # prefix     _  1 12 123
        # suffix 321 32 3 _
        prefix = 1
        for i in range(0, len(nums), 1):
            res[i] *= prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res
