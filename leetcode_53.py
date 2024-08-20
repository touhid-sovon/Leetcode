class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = nums[0]
        cur_sum = 0
        l = 0
        r = 0

        for i, num in enumerate(nums):
            if cur_sum < 0:
                cur_sum = 0
                l = i
                r = i
            cur_sum += num
            if cur_sum > max_sum:
                max_sum = cur_sum
                r = i

        return l, r, max_sum


sol = Solution()
arr = [13, -3, -25, 20, -3, -16, -23, -18, 20, -7, -5, -22, 15, -4, 7]
print(sol.maxSubArray(arr))
