class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # track the first value in case its the smallest (every number might be negative, so need something to compare other negs to cant do 0)
        res = nums[0]
        total = 0
        for n in nums:
            # add the current number to our total
            total += n
            # if adding that number would make our result negative, then it would not be worth to take it, since it would cancel everything before it
            res = max(res, total)
            if total < 0:
                # reset total to 0, basically resetting our process
                total = 0
        return res
