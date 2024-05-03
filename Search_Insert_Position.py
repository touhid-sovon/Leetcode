import bisect

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        #return (bisect.bisect_left(nums,target))
        lo = 0
        hi = len(nums)

        while lo < hi:
            mid = (lo + hi) // 2
            if  target > nums[mid]:
                lo = mid + 1
            else:
                hi = mid

        return lo


solution = Solution()

print(solution.searchInsert([1,3,3,3,7,10],3))

