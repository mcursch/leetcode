class Solution:
    def maxArea(self, height: List[int]) -> int:
        # track max result as you iterate through
        resMax = 0
        # classic two pointer approach, one at left, one at right(end)
        l, r = 0, len(height) - 1

        while l < r:
            # calculate cur width, height, and max area
            width = r - l
            cur_height = min(height[r], height[l])
            resMax = max(resMax, width * cur_height)

            # we want to keep the larger pillars, because theyll always give max volume compared to smaller pillars
            if height[r] < height[l]:
                r -= 1
            else:
                l += 1
        return resMax
