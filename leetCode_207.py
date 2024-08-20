import collections


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # adjacencyList
        preMap = {i:[] for i in range(numCourses)}

        for course, pre in prerequisites:
            preMap[course].append(pre)

        visitSet = set()

        def dfs(course):
            if course in visitSet:
                return False
            if preMap[course] == []:
                return True

            visitSet.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            visitSet.remove(course)
            preMap[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course): return False
        return True

sol = Solution()
pre = [[0,1],[0,2],[1,3],[1,4],[3,4]]
print(sol.canFinish(5,pre))
