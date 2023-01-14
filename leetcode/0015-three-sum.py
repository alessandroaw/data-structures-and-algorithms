# two pointer
# TC: O(n)
# SC: O(n)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # def twoSum(tnums:List[int], target) -> List[int]:
        # iterate through the list O(n)
        #   first pointer in x
        #   twoSum target number = -x O(n2)
        #   twoSum problem with target -x
        #       second pointer in y
        #       last target = y + x
        # O(n3) threeSum --> twoSum
        # Sort O(n log n), threeSum O(n) --> twoSum O(n)
        res = []
        nums.sort()

        def twoSum(tnums: List[int], t: int) -> List[int]:
            out = []
            l, r = 0, len(tnums) - 1

            while l < r:
                currSum = tnums[l] + tnums[r]
                if currSum > t:
                    r -= 1
                elif currSum < t:
                    l += 1
                else:
                    out.append([tnums[l], tnums[r]])
                    prevL = tnums[l]
                    while l < r and tnums[l] == prevL:
                        l += 1

            return out

        prev = nums[0] - 1
        for i, n in enumerate(nums):
            if n > 0:
                break
            if prev == n:
                continue
            tsum_pairs = twoSum(nums[i+1:], -n)
            for pair in tsum_pairs:
                res.append([n, *pair])
            prev = n

        return res
