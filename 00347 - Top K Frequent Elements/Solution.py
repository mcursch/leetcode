class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a number counter
        counter = {}
        # create 2d array of empty values to store each count
        freq = [[] for i in range(len(nums) + 1)]

        # use number counter to get count of each number
        for n in nums:
            counter[n] = 1 + counter.get(n, 0)

        # use freq array to mark each count. ex, 5 item array will have highest count 5, so need to make arr of length 6 to hold 0-5
        # add each number as an arr item of the index matching its count
        for number, count in counter.items():
            freq[count].append(number)

        res = []
        # go backwards through the freq array (highest occuring characters will be in the back)
        # do res += freq[i] for shorter code so you dont have to check if freq[i] = [] (no numebrs have that freq)
        for i in range(len(freq) - 1, -1, -1):
            # if not freq[i]:
            #     pass
            # else:
            #     res.extend(freq[i])
            res += freq[i]
            if len(res) == k:
                return res