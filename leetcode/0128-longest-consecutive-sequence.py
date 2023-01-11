# array and hashing
# TC: O(n)
# SC: O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        s = set(nums)
        max_count = 1

        for n in s:
            # check if its a head
            if not n-1 in s:
                count = 1
                while n + count in s:
                    count += 1
                max_count = max(max_count, count)

        return max_count
