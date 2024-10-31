class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # my solution, works and passes
        # go through each char in the first string
        # check if each string in the array has that char at that index
        # return curr res if not, append char to res if it completes
        res= ""
        s = strs[0]
        for i in range(len(s)):
            for item in strs:
                if i > len(item)-1 or s[i] != item[i]:
                    return res
            res += s[i]
        return res

        # optimal solution
        # sort the array of strings, can just comare the first and last values since shortest is bottleneck
        ans=""
        v=sorted(v)
        first=v[0]
        last=v[-1]
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return ans
            ans+=first[i]
        return ans