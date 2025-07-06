class Solution(object):
    def maxSubArray(self, nums):
        max_sum = cur_sum = nums[0]
        for num in nums[1:]:
            cur_sum = max(cur_sum, 0) + num
            max_sum = max(max_sum, cur_sum)

        return max_sum
