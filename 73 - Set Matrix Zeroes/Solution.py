class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # brute force, make a copy array, modify each value in the copy
        # more effective: use length m arr to track 0 cols, length n arr to track 0 rows
        # most effective: put those length m and length n arrays into the matrix (row 1 and col 1)
        # notice that they would overlap at 0,0 so we need 1 extra variable to store that, but still O(1)
        # works because we only set values to cells that we already visited

        # get rows and cols
        ROWS, COLS = len(matrix), len(matrix[0])

        # track our 0,0 val
        rowZero = False

        # go through, marking valus where they need to be zerod
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True

        # now go through and set values to be zero, but dont do 1st row or col, because theyre special
        for r in range(1, ROWS):
            for c in range(1, COLS):
                # if cols ned to be zerod or rows need to be zerod
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # now do first col (to set cols, go through each row)
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        # now do first row ( to set row, go through cols)
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0

