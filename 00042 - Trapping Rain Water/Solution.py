class Solution:
    def trap(self, height: List[int]) -> int:
        # use two pointer approach, with a left max and right max to store the max heights as you go through
        res = 0
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]

        while l < r:
            if leftMax < rightMax:
                # since lmax is less than rmax, we know that whatever we need to do, we can always store at most lmax water, because rmax is > lmax, so its allowed
                # we also need to check current height, which is why we subtract it from lmax to get water stored
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res
