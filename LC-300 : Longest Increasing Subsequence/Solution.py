class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # establish LIS array, we will init to 1 because every num will have at least one lis
        # each element in the array is the LIS starting at that position
        LIS = [1] * len(nums)

        # last position will always be 1, we will use as a base and build from there
        # start at end, and decrement down
        for i in range(len(nums) - 1, -1, -1):
            # go from the current i position to the end of the array
            # we do this to compare each value in the array to the vals in front of it
            # if a value is less than any val in front of it, we can attach it to the LIS
            # of that number. For this problem, we want the MAX LIS, so we will take the max of
            # these comparison values
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    # this num is valid to extend, so if it can, extend it
                    # we compare the max of the current LIS, so in case we need to replace
                    # a smaller LIS with a bigger one
                    # we also compare to 1 + LIS[j], which is the act of extending and adding cur
                    # to that LIS
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        # return the max of LIS
        return max(LIS)