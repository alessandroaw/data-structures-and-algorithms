# two pointer
# TC: O(n)
# SC: O(1)

class Solution:
    def trap(self, height: List[int]) -> int:
        water_area = 0
        l, r = 0, len(height) - 1
        maxLeft, maxRight = height[l], height[r]

        while l < r:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(maxLeft, height[l])
                water_area += maxLeft - height[l]
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                water_area += maxRight - height[r]

        return water_area
