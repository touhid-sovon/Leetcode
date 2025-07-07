class Solution(object):
    # def alternatingSubarray(self, nums):
    #     n = len(nums)
    #     max_len = -1
    #     cur_len = -1
    #     for i in range(1,n):
    #         if nums[i] - 1 == nums[i-1]:
    #             cur_len = 2
    #             for j in range(i+1,n,2):
    #                 if nums[j] == nums[i-1]:
    #                     cur_len += 1
    #                     if j+1< n and nums[j+1] == nums[i]:
    #                         cur_len += 1
    #                     else:
    #                         break
    #                 else:
    #                     break
    #
    #         max_len = max(max_len,cur_len)
    #
    #     return max_len

    def alternatingSubarray(self,nums):
        n = len(nums)
        max_len = -1

        for i in range(n - 1):
            if nums[i + 1] - nums[i] == 1:
                length = 2
                j = i + 2
                # alternate between nums[i] and nums[i+1]
                while j < n and nums[j] == nums[j - 2]:
                    length += 1
                    j += 1
                max_len = max(max_len, length)

        return max_len


sol = Solution()
print(sol.alternatingSubarray([1,2,2,3,2,2,2,3,2]))



