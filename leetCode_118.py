class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = []
        for i in range(1,numRows+1):
            if i == 1:
                res.append([1])
            elif i == 2:
                res.append([1,1])
            else:
                nth_res = res[-1].copy()
                for j in range(1,len(nth_res)):
                    nth_res[j] = res[-1][j] + res[-1][j-1]
                nth_res.append(1)
                res.append(nth_res)

        return res

sol = Solution()
print(sol.generate(7))


