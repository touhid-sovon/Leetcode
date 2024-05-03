class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        n = -(len(digits)) - 1
        sum = 0
        pro = 1

        for i in range(-1, n, -1):
            sum = sum + digits[i] * pro
            pro *= 10

        sum += 1

        nums2 = []
        print(sum)
        while sum > 0:
            nums2.append(sum % 10)
            sum = sum // 10

        nums2.reverse()

        return nums2

