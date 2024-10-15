class Solution:
    def countSubstrings(self, s: str) -> int:
        #initialize any neede variable
        #count variable will track the number of palindromes
        count = 0

        #go through each index in the len of string (need to access each character)
        for i in range(len(s)):
            #need to track even and odd length palindromes, so use two while's
            #whiles do the same thing: track if OOB and valid palindrome. if so, inc count
            #and move l and r pointers

            #odd length, start l and r at the same index
            l,r = i, i
            while l >= 0 and r < len(s) and s[r] == s[l]:
                count +=1
                l -= 1
                r += 1

            #even length, start l and r at adjacent indices
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[r] == s[l]:
                count +=1
                l -= 1
                r += 1

        #return final count
        return count
