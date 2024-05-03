# class Solution:
#     def maxSubArray(self, nums: list[int]):
#         if len(nums) == 1:
#             return sum(nums)
#
#         max_sub = []
#         prev_sum = nums[0]
#         start,end,cur_sum = 0,1,0
#
#         while end<=len(nums):
#             cur_sum = sum(nums[start:end])
#             print(f"Start:{start} ,End:{end},Cur_sum:{cur_sum},Prev_sum:{prev_sum}")
#
#
#             while start < end and cur_sum > prev_sum:
#                 prev_sum = cur_sum
#                 start += 1
#                 max_sub.append(cur_sum)
#                 prev_sum = max_sub[-1]
#             end += 1
#
#
#
#
#         return max(max_sub)
#
#
# # nums = [1,2,3,4,5,6]
# # new_arr = []
# # new_arr.append(nums[2:4])
# #
# # print(new_arr)
#
#
# sol = Solution()
#
# print(sol.maxSubArray([5,4,-1,7,8])

class Solution:
    def maxSubArray(self,nums:list[int]) -> int:
        max_sum = nums[0]
        cur_sum = 0

        for n in nums:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += n
            max_sum = max(max_sum,cur_sum)

        return max_sum

sol = Solution()

print(sol.maxSubArray([2,3,-2,4]))

