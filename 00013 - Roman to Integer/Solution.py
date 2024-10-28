class Solution:
    def romanToInt(self, s: str) -> int:
        # make hashmap of chars
        roman_to_int = { 'I' : 1 , 'V': 5 , 'X': 10 , 'L': 50 , 'C': 100 , 'D': 500 , 'M': 1000 }
        value = 0
        # go through each index and char in s
        for i,c in enumerate(s):
            # if in range, and the curr char is less than the next one, we have to subtract
            if i + 1 < len(s) and roman_to_int[s[i]] < roman_to_int[s[i+1]]:
                value -= roman_to_int[c]
            # else, just add
            else:
                value += roman_to_int[c]
        return value