class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for char in columnTitle:
            val = ord(char) - ord('A') + 1
            res += res * 25 + val

        return res

sol = Solution()
print(sol.titleToNumber('AA'))
