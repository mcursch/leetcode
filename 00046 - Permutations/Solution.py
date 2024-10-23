class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(arr):
            # reached our base case
            if arr == []:
                return [[]]
            res = []
            # do this until we get to base case
            perms = dfs(arr[1:])
            for p in perms:
                # go + 1 here because we want to add to the end of the array
                for i in range(len(p) + 1):
                    # make a copy of p so we dont mess up the other permutations i.e. if we add 1 to 2,3 and get 1,2,3, then try again in the mid, wed get 1,2,1,3
                    p_copy = p.copy()
                    # only add nums[0] because we removed that, so were adding it back in as we backtrack
                    # so nums owuld be 2,3 but we would only add 2 to [3] that returned
                    p_copy.insert(i, arr[0])
                    # append the generated permutation to teh result
                    # do it inside here because each iteration of this generates a sub perm which needs to get returned
                    res.append(p_copy)
            return res

        return dfs(nums)



