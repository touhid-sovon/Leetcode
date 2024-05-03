# class Solution:
#     def maxSubArrayProduct(self,nums:list[int]) -> int:
#         max_prod = nums[0]
#         cur_prod = 1
#
#         for n in nums:
#             if cur_prod < 0:
#                 cur_prod = 1
#             cur_prod *= n
#             max_prod = max(max_prod,cur_prod)
#
#         return max_prod
#
# sol = Solution()
# print(sol.maxSubArrayProduct([-3,-1,-1]))

# Brute force
#
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        max_prod = max(0,nums[0])
        cur_prod = 1
        neg_buffer = 1
        neg_product = 0
        for n in nums:
            cur_prod = cur_prod * n
            max_prod = max(max_prod, cur_prod)
            if cur_prod <= 0:
                #1,-1,1,1,1,-4,-1,-4
                neg_buffer = neg_buffer * cur_prod
                cur_prod = 1
                if neg_buffer > 0:
                    neg_product = neg_buffer


        return max(max_prod,neg_product)

sol = Solution()
#print(sol.maxProduct([1,-1,1,1,1,-4,-1,-4]))
print(sol.maxProduct([1,0,2,]))
print(sol.maxProduct([-1,0,-2]))
print(sol.maxProduct([-2,-3,7]))






