class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        for i,num  in enumerate(nums):
            if i > 0 and (num == nums[i-1]):
                continue
            left,right = i+1,len(nums)-1

            while left<right:
                threeSome = num + nums[left] + nums[right]
                if threeSome > 0:
                    right -= 1
                elif threeSome < 0:
                    left += 1
                else:
                    res.append([num,nums[left],nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        return res

sol = Solution()
print(sol.threeSum([-2,0,1,1,2]))




