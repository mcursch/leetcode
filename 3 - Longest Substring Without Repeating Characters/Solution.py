class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # utilize a set because they have easy add and removal properties
        charSet = set()
        l = 0
        res = 0

        # go through each value in arr as r pointer
        for r in range(len(s)):
            # if the current value is in our set, remove it and increment the left pointer to slide the window over
            # need to check for duplicates first
            while s[r] in charSet:
                charSet.remove(s[l])
                l +=1
            # if the char is unique, add it in
            charSet.add(s[r])
            # after adding, calculate the max length, which is r - 1 +1. if l is the beginning (0), r is 1, and weve added, res would be 2, aka length of 2 ss
            res = max(res, r-l +1)
        return res