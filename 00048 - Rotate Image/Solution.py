class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # set l and r, nxn so r can just be len -1
        l, r = 0, len(matrix) - 1

        # if l < r, we are either at l == r (1x1, no need to rotate) or l < r (for even matrix), so stop
        while l < r:
            # r - l gives iteration count ex: 4x4, want to do 3 iterations (dont do last so we dont replace it), l = 0, r = 3, 3-0
            # when we increement, we have a 2x2, so we only need to do 1 iteration, r - l = 2-1 = 1
            # use i too increement which elements are actually being removed
            for i in range(r - l):
                # get top and bottom pointers
                # we can do this since n x n, so top will be 0 (to start), and bottom will be len(arr) -1, equal to r
                top, bottom = l, r

                # as we go through array, we have to increment to continue shifting the shell ( think of it as spinning the "square" 45 degress)
                # save top left
                temp = matrix[top][l + i]

                # replace top left with bottom left
                matrix[top][l + i] = matrix[bottom - i][l]

                # replace bottom left with bottom right
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # replace bottom right with top right
                matrix[bottom][r - i] = matrix[top + i][r]

                # replace top right with top left (stored in temp)
                matrix[top + i][r] = temp
            l += 1
            r -= 1

