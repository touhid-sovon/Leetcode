# class Solution:
#     def findMin(self, nums: list[int]) -> int:
#         min_num = min(nums)
#         return min_num
#
#
# arr1 = [4,5,6,7,0,1,2]
# sol = Solution()
# print(sol.findMin(arr1))
#

#v optmize solution

class Solution:
    def findMin(self,nums:list[int]) ->int:
        l , r = 0, len(nums)-1
        i = 1
        while l < r:
            mid = (l+r)//2
            if nums[mid] > nums[r]:
                l = mid+1
            else:
                r = mid
        return nums[r]

sol = Solution()
print(sol.findMin([11,13,15,17]))
