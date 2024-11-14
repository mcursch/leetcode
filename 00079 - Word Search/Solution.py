class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # path set to track current letters
        path = set()
        # get rows and cols
        ROWS, COLS = len(board), len(board[0])
        # dfs function to go through each coord in grid
        # r tracks row, c tracks col, i tracks current place in word
        def dfs(r,c,i):
            # base cases
            # if lengths equal, we have the word, return true
            if len(path) == len(word):
                return True
            # fail cases
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != word[i] or (r,c) in path:
                return False
            # add cur letter cus its good
            path.add((r,c))
            # recurse
            res = dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or dfs(r,c+1,i+1) or dfs(r,c-1, i+1)
            # remove letters added because in case of false, they might be in wrong order
            # consier case abca. if we start at wrong a, we need to remove that from visit
            # to get the right answer
            path.remove((r,c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True
        return False

