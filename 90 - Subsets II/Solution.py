class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            # choice 1: add current value, dfs next values
            subset.append(nums[i])
            dfs(i + 1)

            # choice 2: dont add it, dfs next values
            subset.pop()
            # once you pop the value, weve already got all the subsets with it, so increment the array while you have duplicates
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            # call dfs. if the last val is a duplicate, this will cancel by oob conditino above
            dfs(i + 1)

        dfs(0)
        return res
