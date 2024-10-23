class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # we have a duplicate, ignore it because we already found its possibilities
            if i > 0 and a == nums[i - 1]:
                continue

            # assign our left and right pointers to the next values
            l, r = i + 1, len(nums) - 1
            while l < r:
                # get the sum
                threeSum = a + nums[l] + nums[r]

                # if tS is greater than 0, it means our values that we added were too big, so make them smaller by decrementing right pointer
                if threeSum > 0:
                    r -= 1

                # if tS is less than 0, it means our values that we added were too small, so make them bigger by incrementing left pointer
                elif threeSum < 0:
                    l += 1
                # else they are 0, add this combination and incremeent the left pointer. keep in mind to avoid duplicates we need to additionally increment

                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res


