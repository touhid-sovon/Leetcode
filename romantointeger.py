class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        result = 0
        i = 0
        while i<n:
            if s[i] == 'I':
                if (i+1) < n and s[i+1] == 'V':
                    result += 4
                    i+=1
                elif (i+1) < n and s[i + 1] == 'X':
                    result += 9
                    i+=1
                else:
                    result += 1

            elif s[i] == 'X':
                if (i + 1) < n and s[i + 1] == 'L':
                    result += 40
                    i+=1
                elif (i + 1) < n and s[i + 1] == 'C':
                    result += 90
                    i+=1
                else:
                    result += 10

            elif s[i] == 'C':
                if (i + 1) < n and s[i + 1] == 'D':
                    result += 400
                    i += 1
                elif (i + 1) < n and s[i + 1] == 'M':
                    result += 900
                    i += 1
                else:
                    result += 100

            elif s[i] == 'V':
                print(i)
                result += 5
            elif s[i] == 'L':
                result += 50
            elif s[i] == 'D':
                result += 500
            elif s[i] == 'M':
                result += 1000
            i += 1
        return result

solution = Solution()
print(solution.romanToInt('MCMXCIV'))








