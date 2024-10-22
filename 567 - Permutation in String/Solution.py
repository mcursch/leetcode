class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1Count, s2Count = [0] * 26, [0] * 26

        # init both Counts to the first n = len(s1) values
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        # go through once to get matches
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: return True

            # get the index value of the current character
            index = ord(s2[r]) - ord('a')
            # increment the s2 window count
            s2Count[index] += 1

            # if the counts now match, inc matches
            if s1Count[index] == s2Count[index]:
                matches += 1
            # if the counts matched before, but dont anymore, dec matches
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            # do the same for removing left side char from window

            # get the index value of the current character
            index = ord(s2[l]) - ord('a')
            # decrement the s2 window count
            s2Count[index] -= 1

            # if the counts now match, inc matches
            if s1Count[index] == s2Count[index]:
                matches += 1
            # if the counts matched before, but dont anymore, dec matches
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1

            # increase left side with right side to keep window same size
            l += 1

        # we dont actually check if matches == 26 on last char, so check it here
        return matches == 26


