# array and hashing
# TC: O(n)
# SC: O(1)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = nums[0]
        i = 1

        while i < len(nums):
            while i < len(nums) and nums[i] == prev:
                nums.pop(i)

            if i < len(nums):
                prev = nums[i]
                i += 1

        return len(nums)
