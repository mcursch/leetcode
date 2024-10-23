class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # dp solution, pretty inefficient though because we have to iterate through each number and see if it can jump
        # dp = [False] * len(nums)
        # dp[len(nums) - 1] = True
        # for i in range(len(nums)-2,-1,-1):
        #     if nums[i] == 0:
        #         dp[i] = False
        #     elif nums[i] > len(nums):
        #         dp[i] = True
        #     else:
        #         for j in range(nums[i]):
        #             if (i+j) < len(nums) - 1 and dp[i+j+1]:
        #                 dp[i] = True
        #                 break
        #             # if (i + j) < len(nums) - 1:
        #             #     dp[i] = dp[i] or dp[i + j + 1]
        # return dp[0]

        #Greedy, move goalpost
        goal = len(nums) -1
        for i in range(len(nums)-1,-1,-1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0
