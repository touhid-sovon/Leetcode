class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        r = len(needle)

        for i in range(len(haystack)):
            if haystack[i:r] == needle:
                return i
            r += 1
        return -1


solution = Solution()
print(solution.strStr("leetcode","leeto"))
