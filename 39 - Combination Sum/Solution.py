class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # utilize recursive approach
        # going to utilize 2 branch decision tree
        # either add the current i value to the array, or add nothing and shrink the array
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i > len(candidates) - 1 or total > target:
                return

            # add current value to cur
            cur.append(candidates[i])
            # dfs with this new canidate
            # i stays the same since we arent restricting array
            # cur is already appended
            # total gets +=  can[i]
            dfs(i, cur, total + candidates[i])

            # now remove canidate
            # dfs without canidate, moving i up by 1
            # total remains the same because we arent adding anything here
            cur.pop()
            dfs(i + 1, cur, total)

        # call dfs
        dfs(0, [], 0)
        return res