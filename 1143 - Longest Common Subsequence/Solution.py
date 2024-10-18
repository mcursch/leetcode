class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # establish a 2D array of zeros 1 larger than the length of t1 and t2
        # each position will hold the length of the longest subsequence in the array
        # by the end, 0,0 will hold the lkongest common subsrq in the entire array
        # as all the values will have been passed back up to it
        # dp = [[0 for j in range(len(text2) +1)] for i in range(len(text1)+1)]

        # #go through in reverse order, calculating each value (bottom up)
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                # if the values are equal, get the diagonal value (means they have the same, so sub-prob is both strings minus first char)
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                # if not equal, then we need to reduce one of the strings. get the max of reducing either string, this accounts for subsequ after a non-match
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        # resutls will bubble back up and to the left, with the final one ending up at [0][0]
        return dp[0][0]

