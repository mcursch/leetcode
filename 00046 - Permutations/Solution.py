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



# more understandable backtracking olution
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        pick = [False] * len(nums)
        def dfs(cur, pick):
            # base case
            # if lengths are equal, weve made it to end and have a permutation, add it
            if len(cur) == len(nums):
                res.append(cur.copy())
            for i in range(len(nums)):
                # if a number hasnt been picked, add it, and configure all perms with it picked
                # after, pop that number, move to next one ( in for loop ) and pick that one
                # always pop and reset a number after picking it
                if not pick[i]:
                    pick[i] = True
                    cur.append(nums[i])
                    dfs(cur, pick)
                    cur.pop()
                    pick[i] = False

        dfs([], pick)
        return res
