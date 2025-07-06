class Solution(object):
    def lengthOfLastWord(self, s):
        result = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] != " ":
                result += 1
            elif result:
                return result

        return result
