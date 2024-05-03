# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         count = 0
#         while n > 0:
#             if n % 10 == 1:
#                 count += 1
#             n =n // 10
#         return count
#
#
# sol = Solution()
# print(sol.hammingWeight(0b00000000000000000000000000001011))
#

n1 = 7
bit = n1 & 1
print(bit)