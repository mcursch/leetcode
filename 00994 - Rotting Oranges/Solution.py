class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # utilize q and bfs because oranges can have multiple rot sources, meaning we need to
        # track them simultaneously
        def bfs():
            q = collections.deque()
            time, fresh = 0, 0

            ROWS, COLS = len(grid), len(grid[0])

            # go through once, adding fresh orangs to fresh count (for end check)
            # also append any rotten oranges to q
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 2:
                        # orange is rotten
                        q.append([r, c])
                    elif grid[r][c] == 1:
                        fresh += 1

            while q and fresh > 0:
                # utilize mini for loop here because we want to go through each iteration and track time
                # if we just do while q we cant track the time properly
                for i in range(len(q)):
                    r, c = q.popleft()
                    # check four directions
                    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                    for dr, dc in dirs:
                        row, col = r + dr, c + dc
                        # if inbounds and valid, rot the orange
                        if (row in range(len(grid)) and col in range(len(grid[0])) and grid[row][col] == 1):
                            grid[row][col] = 2
                            q.append([row, col])
                            fresh -= 1
                time += 1
            # if any fresh oranges left, we couldnt reach them, so return -1
            return time if fresh == 0 else -1

        return bfs()





