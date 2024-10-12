class Solution:
    """ BFS"""
    def numIslands2(self, grid: list[list[str]]) -> int:
        Rows = len(grid)
        Cols = len(grid[0])
        visit = set()
        res = 0
        def is_island(r,c,visit):
            while 1:
                if grid[r][c] == "0" or (r,c) in visit:
                    return 0

                visit.add((r,c))
                neighbours = [(1,0),(-1,0),(0,-1),(0,1)]
                for dr,dc in neighbours:
                    t_r = r + dr
                    t_c = c + dc
                    if 0 <= t_r < Rows and 0 <= t_c < Cols:
                        is_island(t_r,t_c,visit)

                break
            return 1

        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] != "0" or (r,c) not in visit:
                    res += is_island(r,c,visit)

        # print(visit)
        return res
    """ DFS """

    def numIslands(self, grid: list[list[str]]) -> int:


sol = Solution()
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(sol.numIslands(grid))
