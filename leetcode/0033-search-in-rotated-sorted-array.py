class Solution:
    def search(self, nums: List[int], target: int) -> int:

        inflection_point = 0

        prev = nums[0]

        for i in range(len(nums)):
            if nums[i] < prev:
                inflection_point = i
                break

        search_nums = [*nums[inflection_point:], *nums[:inflection_point]]

        left = 0
        right = len(search_nums) - 1

        while left <= right:
            mid = (left + right) // 2
            current = search_nums[mid]

            if target < current:
                right = mid - 1
            elif target > current:
                left = mid + 1
            else:
                return (mid + inflection_point) % len(nums)

        return -1
