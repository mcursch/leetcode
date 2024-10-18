class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #establish memo set to track memoization
        memo = {}
        #dfs function to break down subtrees
        def dfs(text):
            #check if the current problem (or subproblem) is in our memo, return if so
            if text in memo:
                return memo[text]
            #base case: if empty string, weve successfully removed everything, return true
            if text == "":
                return True
            #go through each word in the given wordDict
            for word in wordDict:
                #if that word is a prefix of the current word, replace it
                if text.startswith(word):
                    new = text[len(word):]
                    #recursively call dfs on the new sub problem
                    if(dfs(new)):
                        #if we get true out of the subproblem, we know we can return true
                        memo[text] = True
                        return True
            #if we reach here, weve tried every word. in the dict, and none work, so
            #text cannot be possible to construct. dead end. return false
            memo[text] = False
            return False
        #call on entire string
        return dfs(s)