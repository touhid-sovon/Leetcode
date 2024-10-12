

class Solution:
    """ Brute Force"""
    # def pacificAtlantic(self,heights:list[list[int]])->list[list[int]]:
    #     if not heights:
    #         return []
    #
    #     Row = len(heights)
    #     Column = len(heights[0])
    #
    #     res = []
    #
    #     def can_reach_occean(r,c,occean):
    #         stack = [(r,c)]
    #         visited = set(stack)
    #
    #         while stack:
    #             cr,cc = stack.pop()
    #
    #             if occean == 'pacific' and (cr == 0 or cc == 0):
    #                 return True
    #             if occean == 'atlantic' and (cr == Row-1 or cc == Column-1):
    #                 return True
    #
    #             neighbours = [(0,1),(0,-1),(1,0),(-1,0)]
    #             for dr,dc in neighbours:
    #                 tr = cr + dr
    #                 tc = cc + dc
    #
    #                 if 0 <= tr < Row and 0 <= tc < Column and (tr,tc) not in visited and (
    #                         heights[tr][tc] <= heights[cr][cc]):
    #                     stack.append((tr,tc))
    #                     visited.add((tr,tc))
    #
    #         return False
    #
    #
    #     for row in range(Row):
    #         for col in range(Column):
    #             if can_reach_occean(row,col,"pacific") and can_reach_occean(row,col,"atlantic"):
    #                 res.append([row,col])
    #     return res
    ''' Optimal'''
    def pacificAtlantic(self,heights:list[list[int]])-> list[list[int]]:
        Rows = len(heights)
        Cols = len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(r,c,vistied):
            neighbours = [(1,0),(-1,0),(0,1),(0,-1)]
            for dr,dc in neighbours:
                tr = r + dr # traversing row and column
                tc = c + dc
                if 0<=tr<Rows and 0<=tc<Cols and (tr,tc) not in vistied and (
                    heights[tr][tc] >= heights[r][c]):
                    vistied.add((tr,tc))
                    dfs(tr,tc,vistied)

        # pacific occean border
        for c in range(Cols):
            pacific.add((0,c))
            dfs(0,c,pacific)

        for r in range(Rows):
            pacific.add((r,0))
            dfs(r,0,pacific)

        # from the atlantic occean border
        for c in range(Cols):
            atlantic.add((Rows-1,c))
            dfs(Rows-1,c,atlantic)

        for r in range(Rows):
            atlantic.add((r,Cols-1))
            dfs(r,Cols-1,atlantic)


        return list(set.intersection(pacific,atlantic))




heights = [
  [1, 2, 2, 3, 5],
  [3, 2, 3, 4, 4],
  [2, 4, 5, 3, 1],
  [6, 7, 1, 4, 5],
  [5, 1, 1, 2, 4]
]

sol = Solution()
print(sol.pacificAtlantic(heights))


