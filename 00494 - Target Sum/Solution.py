class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # utilize memoization
        memo = {}

        def dfs(index, total):
            # check memo
            if (index, total) in memo:
                return memo[(index, total)]

            # check base case: if we're at the end of the array, return 1 (way) if the total is equal to the target
            if index == len(nums):
                return total == target

            # else, recursively get the ways if you were to add the cur num or subtract the cur num
            memo[(index, total)] = dfs(index + 1, total + nums[index]) + dfs(index + 1, total - nums[index])
            return memo[(index, total)]

        res = dfs(0, 0)
        return res