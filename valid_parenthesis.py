class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        first, second, third = 0,0,0

        for i in range(n):
            if s[0] == ')' or s[0] =='{' or s[0] == '[':
                return False
            elif s[i] == '(':
                first += 1
            elif s[i] == '{':
                second += 1
            elif s[i] == '[':
                third += 1
            elif first == 1 and second == 0 and third == 0 and s[i] == ')':
                first -= 1
            elif first == 0 and second == 1 and third == 0 and s[i] == '}':
                first -= 1
            elif first == 0 and second == 0 and third == 1 and s[i] == ']':
                first -= 1


        return True

solution = Solution()
print(solution.isValid("(){}[]"))

