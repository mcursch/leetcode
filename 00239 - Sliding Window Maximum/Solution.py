class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # basic inefficient solution
        # res = []
        # for i in range(len(nums) - k + 1):
        #     temp_max = -99999999
        #     for j in range(i, i + k):
        #         temp_max = max(temp_max, nums[j])
        #     res.append(temp_max)
        # return res

        # linear timer
        q = collections.deque()
        res = []
        l = r = 0
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # in case your l is greater than ur q 0 value, which means q 0 is no longer in window, pop it
            if l > q[0]:
                q.popleft()
            if (r+1) >= k:
                # q[0] should be the max value in this window because:
                # we popped everything less than it in the above step
                # we popped anything not in the window
                res.append(nums[q[0]])
                l +=1
            r +=1
        return res