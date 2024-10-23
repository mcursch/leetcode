class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # two solutions, sum entire array and subtract sum from sequence, or xor each value
        # a number XOR by itself will be 0. So if we XOR every number in the range (including our missing val). this produces a "filter" number
        # and then XOR that entire group with our given nums, then everything will become zero except the number we want
        answer = 0
        n = len(nums)
        for i in range(1, n + 1):
            answer ^= i
        for num in nums:
            answer ^= num
        return answer

