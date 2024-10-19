class Solution:
    def isPalindrome(self, s: str) -> bool:
        #init two pointers, one at beginning of s and one at end of s
        l, r = 0, len(s) - 1

        #if the left is less than the right, we are done
        # dont need to check equals, because if l == r, we are at one char, and a char will equal itself.
        while l < r:
            #if either left or right chars are invalid i.e. whitespace, commas, periods, etc, move the respective pointer to get rid of them
            if s[l].isalpha() == False and s[l].isdigit() == False:
                l +=1
            elif s[r].isalpha() == False and s[r].isdigit() == False:
                r -= 1
            # to take care of uppercase, just make each char upper when comparing
            # if the chars arent equal, return false
            elif s[l].upper() != s[r].upper():
                return False
            # in the case two chars are equal, continue via increementing and decrementing
            else:
                l += 1
                r -= 1

        return True