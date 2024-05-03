class Solution:
    def climbStairs(self, n: int) -> int:
        mem = [1,2]
        sum = 0
        for i in range(n):
            if i == 0:
                sum =  mem[i]
            elif i == 1:
                sum = mem[i]
            else:
                sum = mem[i-1] + mem[i-2]
                mem.append(sum)
        return sum

sol = Solution()
print(sol.climbStairs(6))
