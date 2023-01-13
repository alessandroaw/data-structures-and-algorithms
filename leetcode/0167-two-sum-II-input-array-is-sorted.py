# two pointer
# TC: O(n)
# SC: O(1)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # iterate for each number do we have a pair that makes a target
        # current x
        # number we want to find is target - x

        l, r = 0, len(numbers) - 1

        while l < r:
            currSum = numbers[l] + numbers[r]

            if currSum > target:
                r -= 1
            elif currSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
