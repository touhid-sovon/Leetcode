class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        start,end = 0,1
        substring = s[0]
        substring_length = [1]
        while end < len(s):
            if s[end] in substring:
                start += 1
                end = start
                substring = s[start]
            else:
                substring = (s[start:end + 1])
                substring_length.append(len(substring))
            end += 1

        return max(substring_length)

solution = Solution()
print(solution.lengthOfLongestSubstring('pwwkew'))


# s = 'abcd'
# start = 0
# end = 0
# while end<len(s):
#     print(s[start:end+1])
#     end += 1
