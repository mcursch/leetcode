class Solution:
    def jump(self, nums: List[int]) -> int:
        # greedy solution
        # utilize left and right pointe
        l, r = 0, 0
        res = 0
        # while our left pointer is less than last index (while we arent at goal)
        while r < len(nums) - 1:
            maxJump = 0
            # get the maxJump distance by going through each value and computing the max distance we can jump
            for i in range(l, r + 1):
                maxJump = max(maxJump, i + nums[i])
            # l becomes the next value after our current (fine because were guarenteed a solution)
            # r becomes the furthest we could jump
            # expandable window
            l = r + 1
            r = maxJump
            res += 1
        return res
