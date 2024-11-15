class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # to get linear time and constant space
        # use prefix and suffix strat.
        # go up the array, storing at each point in res, the prod of values before it
        # do the same thing going backwards with suffix
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
