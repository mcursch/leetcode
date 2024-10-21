class Solution:
    def rob(self, nums: List[int]) -> int:

        # pretty optimal, but uses O(n) space
        dp = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                dp[i] = nums[i]
            elif i == 1:
                dp[i] = max(nums[i], nums[i - 1])
            else:
                dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        return dp[len(nums) - 1]

        # uses O(1) space
        skip_total, prev_total = 0, 0
        for n in nums:
            # either we keep the previous value, or we skip it and take the current plus the values after skip
            temp = max(prev_total, n + skip_total)
            skip_total = prev_total
            prev_total = temp
        return prev_total
