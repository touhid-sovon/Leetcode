class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        def dfs(i,cur,total):
            if total == target:
                res.append(cur[:])

            if i >= len(candidates) or total >= target:
                return

            cur.append(candidates[i])
            #print(i, cur, total,total+candidates[i],res)
            dfs(i,cur,total+candidates[i])
            cur.pop()
            dfs(i+1,cur,total)

        dfs(0,[],0)

        return res


sol = Solution()
candidates = [2,3,6,7]
target = 7
print(sol.combinationSum(candidates,target))

