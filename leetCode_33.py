class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left , right = 0, len(nums) -1
        while left<=right:
            mid = (left+right) //2
            print(nums[left],nums[mid],nums[right])
            if target == nums[mid]:
                return mid
            # for left sorted portion
            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid+1
                else:
                    right = mid-1
            # for right sorted portion
            else:
                if target < nums[mid] or target >= nums[left]:
                    right = mid-1
                else:
                    left = mid+1
        return -1

sol = Solution()

print(sol.search([4,5,6,7,0,1,2],5))
