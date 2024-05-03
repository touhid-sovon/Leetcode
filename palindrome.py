# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         str1 = str(x)
#         left = 0
#         right = len(str1)-1
#
#         while left < right:
#             if str1[left] != str1[right]:
#                 return False
#             left += 1
#             right -= 1
#         return True
#
# solution = Solution()
# print(solution.isPalindrome(10))


'''solution 2'''

# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         str1 = str(x)
#         if str1 == str1[::-1]:
#             return True
#         else:
#             return False

''' Solution 3 '''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        temp = x
        reverse = 0
        while temp > 0:
            digit = temp % 10
            reverse = reverse * 10 + digit
            temp = temp//10
        print(reverse)
        return reverse == x


solution = Solution()
print(solution.isPalindrome(1234))


