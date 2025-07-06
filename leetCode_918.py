class Solution(object):
    ''' Brute Force -- TLE'''

    # def maxSubArray(self, nums):
    #     n = len(nums)
    #     max_sum = nums[0]
    #     for i in range(n):
    #         cur_sum = 0
    #         for j in range(n):
    #             k = (i + j) % n
    #             cur_sum = max(cur_sum, 0) + nums[k]
    #             max_sum = max(max_sum, cur_sum)
    #
    #     return max_sum

    # def minSubArray(self,nums):
    #     min_sum = nums[0]
    #     cur_sum = 0
    #     for num in nums:
    #         cur_sum += num
    #         cur_sum = min(cur_sum,num)
    #         print(f'Curr Sum: {cur_sum}')
    #         min_sum = min(cur_sum,min_sum)
    #         print(f'Min Sum = {min_sum}')
    #
    #     return min_sum
    def maxSubarraySumCircular(self, nums):
        max_sum = min_sum = nums[0]
        cur_sum = cur_sum_min = total_sum = 0
        for num in nums:
            total_sum += num
            cur_sum = max(cur_sum, 0) + num
            cur_sum_min += num
            cur_sum_min = min(cur_sum_min, num)
            min_sum = min(cur_sum_min, min_sum)
            max_sum = max(cur_sum, max_sum)

        # print(f'Total Sum: {total_sum}|| Max_Sum = {max_sum}|| Min Sum = {min_sum}' )
        if (total_sum == min_sum):
            return max_sum
        return (max(max_sum, (total_sum - (min_sum))))
        # return max_sum if total_sum == min_sum else max(max_sum, total_sum - min_sum)

sol = Solution()

print(sol.maxSubarraySumCircular([-3, -2, -3]))
