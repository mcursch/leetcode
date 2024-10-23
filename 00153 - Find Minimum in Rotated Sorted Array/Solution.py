class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        # cur min cant go above 5000 based on problem constraints, so set its base to something above that that will certainly be replaced
        curr_min = 9999
        # when start and end are equal, we have found our last value
        while start < end:
            middle = (start + end) // 2

            # end value is larger than our current value, so min must be on left side because sorted array means increasing up until then
            curr_min = min(curr_min, nums[middle])
            if nums[middle] < nums[end]:
                end = middle - 1
            else:
                start = middle + 1
        # loop will attempt to gfet smaller and smaller values.
        # however, if the last value is the smallest, start < end will terminate (1 value, start == end), so we have to return the min
        # of our tracked smallest, and whatever the last value is
        return min(curr_min, nums[start])



