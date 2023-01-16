# two pointer
# TC: O(n)
# SC: O(1)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # maximum height * maximum distance
        # we know the absolute maximum distance
        # we don't know the absolute maximum height
        # iterate from the maximum distance to 0, and find the most optimal height
        l, r = 0, len(height) - 1
        max_area = 0

        while l < r:
            curr_h = min(height[l], height[r])
            curr_w = r - l
            curr_area = curr_h * curr_w
            max_area = max(max_area, curr_area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area
