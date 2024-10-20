class Solution:
    def countBits(self, n: int) -> List[int]:
        # using dynamic programming
        # establish array of zeros for dp array
        dp = [0] * (n + 1)
        # use offset value to track what we need to offset our answer ex: dp[8] = 1 + dp[8-8] = 1 +dp[0]
        offset = 1
        # go from 1 to n, allows us to get to final value. can start at 1 because dp[0] already 0 which is correct
        for i in range(1, n + 1):
            # if we have a new highest bit (1,2,4,8,16), set offset to it
            if offset * 2 == i:
                offset = i
            # set current el to previous value plus 1
            dp[i] = 1 + dp[i - offset]
        return dp


