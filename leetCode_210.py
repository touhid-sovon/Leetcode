class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        preMap = { i:[] for i in range(numCourses)}

        for course,pre in prerequisites:
            preMap[course].append(pre)

        visit = set()
        queue = []
        def dfs(course):
            if course in visit:
                return False
            if preMap[course] == []:
                if course not in queue:
                    queue.append(course)
                return True

            visit.add(course)
            for pre in preMap[course]:
                if not dfs(pre): return False
            visit.remove(course)
            if course not  in queue:
                queue.append(course)
            preMap[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course): return []
        return queue


sol = Solution()

prereq = []
print(sol.findOrder(1,prereq))

