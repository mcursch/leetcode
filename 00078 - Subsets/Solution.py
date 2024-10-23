class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # track an index instead, andmove the index as u recursew
        i = 0

        res = []
        subset = []

        def dfs(i):
            print(subset)
            if i >= len(nums):
                # reached the end
                res.append(subset.copy())
                return
            # recurse with nums added
            # make decision to add current member [1,2,3] -> [1] [2,3]
            subset.append(nums[i])
            dfs(i + 1)

            # recurse with nums not added
            # make decision to not add current number [1,2,3] => [] [2,3]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res

