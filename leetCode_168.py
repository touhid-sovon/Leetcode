class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        #alphabet_dict = {i: chr(64 + i) for i in range(1, 27)}
        res = ""
        while columnNumber > 0:
            # adjusting the value if the number is divisible by 26
            columnNumber -= 1

            rem = columnNumber % 26
            res += chr(65 + rem) # 'A' is ASCII 65
            columnNumber //= 26

        return res[::-1]




sol = Solution()

print(sol.convertToTitle(53))