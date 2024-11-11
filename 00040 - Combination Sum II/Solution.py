class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # sort the array to eliminate duplicates
        candidates.sort()
        res = []

        def dfs(i, cur, total):
            # check base cases
            # if total == target
            if total == target:
                res.append(cur.copy())
                return
            # if total > target or end of array
            if total > target or i == len(candidates):
                return

                # branch 1: add the current value
            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])

            cur.pop()
            # continue iterating to remove duplicates
            while i + 1 != len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            # branch 2: dont add the current value
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res