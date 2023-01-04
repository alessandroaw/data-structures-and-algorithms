# array and hashing
# TC: O(1)
# SC: O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # use set to store unique element
        s = set(nums)

        # check if the length of set is smaller than the array (means contains duplicate)
        return len(s) < len(nums)
