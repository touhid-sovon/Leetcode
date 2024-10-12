class Solution:
    def isPalindrome(self, s: str)->bool:
        new_str = ""
        for char in s:
            asc_char = ord(char)
            if 65<= asc_char <= 90:
                new_str += chr(asc_char+32)
            if 97 <= asc_char <= 122:
                new_str += char

        return new_str == new_str[::-1]

s = "A man, a plan, a canal: Panama"
sol = Solution()
print(sol.isPalindrome(s))
