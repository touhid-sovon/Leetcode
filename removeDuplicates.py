class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        unique = 0
        for i in range(1,n):
            if nums[unique] != nums[i]:
                # print(tempList[unique],nums[i])
                unique += 1
                nums[unique] = nums[i]

        return unique+1

solution = Solution()
print(solution.removeDuplicates([1,1,2]))

