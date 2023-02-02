class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]

        curr_sum = nums[0]

        for i in range(len(nums)):
            if i == 0:
                continue
            curr_sum = max(curr_sum + nums[i], nums[i])
            max_sum = max(max_sum, curr_sum)

        return max_sum
