class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # if grid = [] or grid = [[]], return 0 islands
        if not grid or not grid[0]:
            return 0
        # get rows and columns
        rows = len(grid)
        cols = len(grid[0])

        # establish set to track visited elements
        visit = set()

        # island count to be returned at end
        island_count = 0

        # define a dfs function
        def dfs(r, c):
            # if a node (grid[r][c]) is out of bounds, or 0, or already visited, return from the dfs
            if r not in range(rows) or c not in range(cols) or grid[r][c] == '0' or (r, c) in visit:
                return

                # else, that node must be an unvisited 1. add it to the visit list, because its part of the bigger island, we dont inc islkand count
            visit.add((r, c))
            # from the current node, get the four directions we need to check (hardcoded)
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            # recursively check each direction
            # this will get every 1 connected to the current island
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # go through each coord in the array
        for r in range(rows):
            for c in range(cols):
                # this loop finds new islands. if we find one, find all its neighbors, and then continue looking
                # ignore 0's
                if grid[r][c] == "1" and (r, c) not in visit:
                    # we have a new island, increase island count
                    island_count += 1
                    # find all adjacent ones to this island. only call dfs when we have a new island
                    dfs(r, c)
        return island_count



