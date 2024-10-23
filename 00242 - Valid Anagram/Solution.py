class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if the lengths arent equal, cannot be an anagram
        if len(s) != len(t):
            return False

        # initialize two dicts
        # we will be counting each character in the strings, and placing the count of each char in the hashtable
        # after, we will return true if the hashtables are equal.
        countS, countT = {}, {}

        for i in range(len(s)):
            # if the value is in the hash, set the new value to 1 plus that.
            # if not, get() returns zero, so the count gets set to 1+0 = 1
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT

