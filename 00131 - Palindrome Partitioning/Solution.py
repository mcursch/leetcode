class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        def dfs(start):
            # if weve made it to this section, wev successfuly partitoned, so add part to res
            if start == len(s):
                res.append(part.copy())
                return
            # go through each sub of s
            # if the current sub is a pal, add it to part, and continue the dfs from that point on
            # after dfs returns (part over), pop the most recent val, and extend it

            #think of i as ther start value
            # think of j as the range. j sets the partition point if its a pal
            # so for a, j recursively calls this process on ab with a as the start
            for j in range(start, len(s)):
                if self.isPali(s, start, j):
                    part.append(s[start : j + 1])
                    dfs(j + 1)
                    part.pop()

        dfs(0)
        return res

    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True