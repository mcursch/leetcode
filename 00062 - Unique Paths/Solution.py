class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # establish memo object
        memo = {}

        def dfs(r, c):
            # check the memo for faster compute time
            if ((r, c) in memo):
                return memo[(r, c)]
            # we get to a 1x1 grid, 1 solution: do nothing
            if r == 1 and c == 1:
                return 1

            # we are out of bounds
            if r <= 0 or c <= 0:
                return 0
            # store value in memo
            memo[(r, c)] = dfs(r - 1, c) + dfs(r, c - 1)
            return memo[(r, c)]

        return dfs(m, n)

