class Solution:
    def climbStairs(self, n: int) -> int:
        # establish a hastable in order to store values in for fast lookup
        memo = {}

        def dfs(n):
            # if the value is in our memo, return it
            if n in memo:
                return memo[n]
            # base case: if n <= 1, return 1
            # this insinuates theres 1 way to climb a stair with n = 0
            # fine if we assume "doing nothing" to be the one way
            if n <= 1:
                return 1
            # call our subproblems. basically, if get all the ways if we took 1 step and all the ways if we took 2 steps
            # then do this recursively for each other sub problem
            # store this value in the memo for faster lookup, if n = 44, we dont want to have to calculat n = 22 twice
            memo[n] = dfs(n - 1) + dfs(n - 2)
            return memo[n]

        return dfs(n)







