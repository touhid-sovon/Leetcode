class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        ans = ""
        strs.sort()
        first = strs[0]
        last = strs[-1]

        for i in range(min(len(first),len(last))):
            if first[i]!= last[i]:
                return ans
            ans+=first[i]
        return ans


        print(v)


solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"]))
