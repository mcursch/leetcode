class Solution:
    def longestPalindrome(self, s: str) -> str:
        # establish tracker variables for result and length of result
        res = ""
        resLen = 0

        # go through each index of the string (each character)
        for i in range(len(s)):
            # establish two while loops, one for even length palindroms, one for odd

            # odd length palindroms (l and r start at same character)
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # checking if l or r are OOB, and l val equals r val (valid pal)
                if (r - l + 1 > resLen):
                    # if the palindrome is bigger than the current max, store it and update
                    res = s[l:r + 1]
                    resLen = r - l + 1

                l -= 1
                r += 1

                # even length palindromes (l and r start with adjacent characters)
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1 > resLen):
                    res = s[l:r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

        return res
