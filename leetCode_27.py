class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if (nums[i]!=val):
                nums[k] = nums[i]
                k += 1
        return nums[:k]

sol = Solution()

print(sol.removeElement([0,1,2,2,3,0,4,2],2))

# arr1 = [1,2,3,4,5]
#
# arr1.remove(2)
# arr1.pop(2)
# print(arr1)
