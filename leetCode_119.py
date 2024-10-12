class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        pas = []
        for i in range(rowIndex+1):
            if i == 0:
                pas = [1]
            elif i == 1:
                pas = [1,1]
            else:
                tmp = pas.copy()
                for j in range(1,len(tmp)):
                    tmp[j] = pas[j] + pas[j-1]
                tmp.append(1)
                pas = tmp.copy()


        return pas


sol = Solution()
print(sol.getRow(0))

