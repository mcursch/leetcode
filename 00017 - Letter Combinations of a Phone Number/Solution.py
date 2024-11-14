class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # have a map for each number to the three-4 letters it can contain
        # edge case: if digits is nothing, just return res
        # else, backtrack:
        # base case: if len(current_perm) = len(digits): append and return
        # for each char in digits(i):
        # append it
        # dfs (i+1, cur) (begin working on next set)
        # pop it when all the above combinations are done

        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(i, cur):
            if len(cur) == len(digits):
                res.append("".join(cur.copy()))
                return
            for c in digitToChar[digits[i]]:
                cur.append(c)
                dfs(i + 1, cur)
                cur.pop()

        if digits:
            dfs(0, [])
        return res
