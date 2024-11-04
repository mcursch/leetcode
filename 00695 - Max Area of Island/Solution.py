class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # asked to find max area in 2D array where 1's represent islands
        # utilize a bfs to spread and check each island when found, marking it as visited and counting its area

        # instead of using visit set, set visited valeus to 0
        maxArea = 0
        # 4 directions for checking later
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(r, c):
            q = deque()
            curArea = 1
            grid[r][c] = 0
            q.append([r, c])

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    # if we have a 1, look at the 4 adj squares next to it ( U D L R). if they are OOB or 0, skip them (will only pass with inbound 1's)
                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == 0):
                        continue
                    q.append([nr, nc])
                    grid[nr][nc] = 0
                    curArea += 1
            return curArea

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and grid[r][c]:
                    # we have a new island, bfs it to get its area and compare to max
                    maxArea = max(maxArea, bfs(r, c))

        return maxArea
